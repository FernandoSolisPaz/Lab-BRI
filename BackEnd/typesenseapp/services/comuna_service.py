from typesenseapp.repositories import comuna_repository

def obtener_comuna_de_punto(long, lat):
    return comuna_repository.comuna_que_contiene_punto(long, lat)

def listar_comunas():
    return comuna_repository.listar_comunas()

def crear_comuna(nombre, geometria):
    return comuna_repository.guardar_comuna(nombre, geometria)
