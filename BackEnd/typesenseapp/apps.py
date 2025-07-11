from django.apps import AppConfig
import typesense
import os
import json
from dotenv import load_dotenv

class TypesenseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'typesenseapp'
    has_initialized = False  # bandera para evitar ejecuciones múltiples
    
    def ready(self):
        if TypesenseappConfig.has_initialized:
            return
        TypesenseappConfig.has_initialized = True  # evita múltiples ejecuciones

        load_dotenv()

        client = typesense.Client({
            'nodes': [{
                'host': 'localhost',
                'port': 8108,
                'protocol': 'http'
            }],
            'api_key': os.getenv("API_KEY_TYPESENSE"),
            'connection_timeout_seconds': 2
        })

        schema = {
            "name": "noticias",
            "fields": [
                {"name": "id", "type": "string"},
                {"name": "titulo", "type": "string", "facet": True},
                {"name": "ubicacion", "type": "string", "facet": True},
                {"name": "keywords", "type": "string[]", "facet": True},
                {"name": "autores", "type": "string[]"},
                {"name": "fecha_publicacion", "type": "int32", "facet": True},
                {"name": "fecha_extraccion", "type": "int32"},
                {"name": "pagina", "type": "string", "facet": True},
                {"name": "texto", "type": "string", "facet": True}
            ],
            "default_sorting_field": "fecha_publicacion"
        }

        try:
            client.collections['noticias'].delete()
        except Exception:
            pass

        try:
            client.collections.create(schema)
        except Exception:
            pass  # Ya existe, no pasa nada

        ruta_json = os.path.join(os.path.dirname(__file__), '..', 'noticias_modificado.json')
        print(ruta_json)
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                noticias = json.load(f)

            for noticia in noticias:
                try:
                    client.collections['noticias'].documents.create(noticia)
                except Exception as e:
                    print(f"Error cargando noticia: {e}")
        except Exception as e:
            print(f"No se pudo cargar el archivo JSON: {e}")