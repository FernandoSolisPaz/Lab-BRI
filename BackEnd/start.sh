#!/bin/bash

set -e

echo "Actualizando repositorios e instalando dependencias..."
sudo apt-get update -y
sudo apt-get install -y wget curl gnupg libssl1.1 || {
  echo "Error instalando dependencias. ¿Tienes permisos de sudo?"
  exit 1
}

echo "Agregando repositorio oficial de MongoDB 5.0..."
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

sudo apt-get update -y
sudo apt-get install -y mongodb-org

echo "Iniciando MongoDB..."
sudo systemctl start mongod
sudo systemctl enable mongod

echo "Descargando Typesense .deb..."
curl -O https://dl.typesense.org/releases/29.0/typesense-server-29.0-amd64.deb

echo "Instalando Typesense..."
sudo dpkg -i typesense-server-29.0-amd64.deb || sudo apt-get install -f -y

echo "Eliminando paquete .deb..."
rm typesense-server-29.0-amd64.deb

echo "Iniciando Typesense en segundo plano..."
nohup /usr/bin/typesense-server --data-dir /tmp/typesense-data --api-key=123 --listen-port=8108 > typesense.log 2>&1 &

echo "Estado de MongoDB:"
sudo systemctl status mongod --no-pager

echo "Proceso Typesense:"
ps aux | grep typesense-server
# Ejecutar typesense-server en background
./typesense-server --data-dir ./typesense-data --api-key=123 > typesense.log 2>&1 &

pip install django mongoengine dotenv django-cors-headers requests typesense
