import typesense
import os
from dotenv import load_dotenv

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