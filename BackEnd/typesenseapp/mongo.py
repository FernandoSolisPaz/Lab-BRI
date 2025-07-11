from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

conn= connect(
    db=os.getenv("MONGO_DB_NAME"),
    username=os.getenv("MONGO_ROOT_USER"),
    password=os.getenv("MONGO_ROOT_PASS"),
    host=os.getenv("MONGO_ROOT_HOST"),
    port=int(os.getenv("MONGO_ROOT_PORT")),
    authentication_source="admin"
)