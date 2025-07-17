from django.shortcuts import render
from django.http import JsonResponse
from .services import comuna_service
from django.views.decorators.csrf import csrf_exempt

from .client_typesense import client
from .mongo import conn
import typesense
import json
import os
import time
from datetime import datetime
import unicodedata

def epoch_day_range(dt: datetime):
    """Devuelve el rango epoch de un día completo"""
    start = datetime(dt.year, dt.month, dt.day, 0, 0, 0)
    end = datetime(dt.year, dt.month, dt.day, 23, 59, 59)
    return int(time.mktime(start.timetuple())), int(time.mktime(end.timetuple()))

@csrf_exempt
def buscar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'error en formato json'}, status = 400)
    
        # Campo de texto principal para búsqueda de texto completo
        texto = data.get('texto', '')

        # Filtros de busqueda
        filtros = []

        if data.get('titulo'):
            filtros.append(f'titulo:={data["titulo"]}')
        if data.get('ubicacion'):
            filtros.append(f'ubicacion:={data.get('ubicacion')}')
        if data.get('pagina'):
            filtros.append(f'pagina:={data["pagina"]}')

        if data.get('exact_date'):
            # Prioridad: exact_date ignora los otros dos
            start_epoch, end_epoch = epoch_day_range(datetime.fromisoformat(data.get('exact_date')))
            filtros.append(f"fecha_publicacion:[{start_epoch}..{end_epoch}]")
        else:
            if data.get('before_date') and data.get('after_date'):
                be = int(time.mktime(datetime.fromisoformat(data.get('before_date')).timetuple()))
                ae = int(time.mktime(datetime.fromisoformat(data.get('after_date')).timetuple()))
                filtros.append(f"fecha_publicacion:[{ae}..{be}]")
            elif data.get('before_date'):
                be = int(time.mktime(datetime.fromisoformat(data.get('before_date')).timetuple()))
                filtros.append(f"fecha_publicacion:<={be}")
            elif data.get('after_date'):
                ae = int(time.mktime(datetime.fromisoformat(data.get('after_date')).timetuple()))
                filtros.append(f"fecha_publicacion:>={ae}")

        if data.get('keywords'):
            for kw in data['keywords']:
                if kw:
                    filtros.append(f'keywords:=[{kw}]')

        if data.get('autores'):
            for autor in data['autores']:
                if autor:
                    filtros.append(f'autores:=[{autor}]')


        filtro_final = " && ".join(filtros) if filtros else None

        query = {
            'q': texto if texto else '*',
            'query_by': 'titulo, ubicacion, keywords, autores, texto, pagina',
            'per_page': 250
        }
        if filtro_final:
            query['filter_by'] = filtro_final
        print(query)
        try:
            result = client.collections['noticias'].documents.search(query)
            return JsonResponse(result, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Mal tipo de rest'}, status=405)

@csrf_exempt
def listar_comunas(request):
    conn
    print(conn)
    comunas = comuna_service.listar_comunas()

    response = []
    for comuna in comunas:
        response.append({
            "nombre": comuna.nombre,
            "geometria": comuna.geometria
        })

    return JsonResponse(response, safe=False)

@csrf_exempt
def obtener_comuna(request):
    conn
    print(conn)
    nombre = request.GET.get("nombre")
    comuna = comuna_service.obtener_comuna(nombre)
    response = {
        "nombre": comuna.nombre,
        "geometria": comuna.geometria
    }

    return JsonResponse(response, safe=False)

@csrf_exempt
def crear_comuna(request):
    conn
    print(conn)
    data = json.loads(request.body)
    response = comuna_service.crear_comuna(data["nombre"], data["geometria"])
    
    return JsonResponse("ight", safe=False)