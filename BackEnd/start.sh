#!/bin/bash

# --- MongoDB ---
# Si no está instalado, descargar y descomprimir portable MongoDB
if ! command -v mongod > /dev/null; then
  echo "Descargando MongoDB..."
  wget -q https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-6.0.4.tgz
  tar -xzf mongodb-linux-x86_64-ubuntu2004-6.0.4.tgz
  export PATH=$PWD/mongodb-linux-x86_64-ubuntu2004-6.0.4/bin:$PATH
fi

mkdir -p ./data/db

# Arrancar mongod en background
mongod --dbpath ./data/db --bind_ip 127.0.0.1 --port 27017 --fork --logpath ./mongod.log

# --- Typesense ---
# Descargar y ejecutar Typesense Server (ajusta versión y ruta)
if [ ! -f typesense-server ]; then
  wget -q https://dl.typesense.org/releases/0.24.0/typesense-server-linux-amd64.tar.gz
  tar -xzf typesense-server-linux-amd64.tar.gz
fi

# Ejecutar typesense-server en background
./typesense-server --data-dir ./typesense-data --api-key=123 > typesense.log 2>&1 &

pip install django mongoengine dotenv django-cors-headers requests typesense
