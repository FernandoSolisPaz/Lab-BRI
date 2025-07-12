from django.urls import path
from .views import buscar
from .views import listar_comunas
from .views import crear_comuna
from .views import obtener_comuna

urlpatterns = [
    path('', buscar),
    path('/comunas', listar_comunas),
    path('/guardarComuna', crear_comuna),
    path('/obtenerComuna', obtener_comuna)
]
