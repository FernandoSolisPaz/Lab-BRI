from typesenseapp.models.comuna import Comuna

def guardar_comuna(nombre: str, geometria: dict):
    return Comuna(nombre=nombre, geometria=geometria).save()

def obtener_comuna_por_nombre(nombre: str):
    return Comuna.objects(nombre=nombre).first()

def comuna_que_contiene_punto(long, lat):
    punto = {
        "type": "Point",
        "coordinates": [long, lat]
    }
    return Comuna.objects(geometria__geo_intersects=punto).first()

def listar_comunas():
    return list(Comuna.objects.all())