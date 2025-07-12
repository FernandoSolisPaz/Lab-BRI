import json
import os
import requests

archivos = os.listdir()

comunas = []

for comuna in archivos:
    if comuna.endswith(".py"):
        continue
    with open(comuna, "r", encoding="utf-8") as f:
        data = json.load(f)
    com = {
        "nombre": data["features"][0]["properties"]["name"],
        "geometria": data["features"][0]["geometry"]
    }
    comunas.append(com)

for comuna in comunas:
    response = requests.post("http://localhost:8000/buscar/guardarComuna", json=comuna)
    print(f"{comuna["nombre"]}: {response.status_code}: {response.text}")
