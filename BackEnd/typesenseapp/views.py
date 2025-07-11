from django.shortcuts import render
from django.http import JsonResponse
from .services import comuna_service
from django.views.decorators.csrf import csrf_exempt

from .client_typesense import client
from .mongo import conn
import typesense
import json
import os

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
            filtros.append(f'titulo:={json.dumps(data["titulo"])}')
        if data.get('ubicacion'):
            filtros.append(f'ubicacion:={json.dumps(data["ubicacion"])}')
        if data.get('pagina'):
            filtros.append(f'pagina:={json.dumps(data["pagina"])}')

        if isinstance(data.get('fecha_publicacion'), int):
            filtros.append(f'fecha_publicacion:={data["fecha_publicacion"]}')
        if isinstance(data.get('fecha_extraccion'), int):
            filtros.append(f'fecha_extraccion:={data["fecha_extraccion"]}')

        if data.get('keywords'):
            for kw in data['keywords']:
                if kw:
                    filtros.append(f'keywords:=[{json.dumps(kw)}]')

        if data.get('autores'):
            for autor in data['autores']:
                if autor:
                    filtros.append(f'autores:=[{json.dumps(autor)}]')


        filtro_final = " && ".join(filtros) if filtros else None

        query = {
            'q': texto if texto else '*',
            'query_by': 'titulo, ubicacion, keywords, autores, texto, pagina'
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