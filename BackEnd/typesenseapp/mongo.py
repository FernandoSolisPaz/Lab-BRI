from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
conn = connect(host=mongo_uri)