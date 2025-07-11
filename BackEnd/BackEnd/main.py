import typesense
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar el cliente Typesense (conectarlo a docker)
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': 8108,
        'protocol': 'http'
    }],
    'api_key': (os.getenv("API_KEY_TYPESENSE")),
    'connection_timeout_seconds': 2
})

schema = {
    "name": "noticias",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "titulo", "type": "string"},
        {"name": "ubicacion", "type": "string"},
        {"name": "fecha_publicacion", "type": "string", "facet": True}
    ]
    #"default_sorting_field": "titulo"
}

# Eliminar el índice si ya existe
try:
    client.collections['noticias'].delete()
except:
    pass

client.collections.create(schema)

with open("../noticias.json", "r", encoding="utf-8") as f:
    noticias = json.load(f)

for noticia in noticias:
    client.collections['noticias'].documents.create(noticia)

# EJ: Filtrar por ubicación con una búsqueda
result = client.collections['noticias'].documents.search({
    'q': 'Lo Espejo',
    'query_by': 'ubicacion'
})

print(result)
