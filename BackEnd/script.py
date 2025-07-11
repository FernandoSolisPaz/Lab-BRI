import json
from datetime import datetime

# Ruta del archivo JSON original
ruta_entrada = "noticias.json"

# Ruta del archivo donde guardarás el resultado
ruta_salida = "noticias_modificado.json"

# Leer JSON desde el archivo
with open(ruta_entrada, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convertir fechas a timestamp Unix
for item in data:
    item["fecha_extraccion"] = int(datetime.strptime(item["fecha_extraccion"], "%Y-%d-%m %H:%M:%S").timestamp())
    item["fecha_publicacion"] = int(datetime.strptime(item["fecha_publicacion"], "%Y-%d-%m %H:%M:%S").timestamp())

# Guardar el resultado en un nuevo archivo (opcional)
with open(ruta_salida, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Fechas convertidas correctamente.")
