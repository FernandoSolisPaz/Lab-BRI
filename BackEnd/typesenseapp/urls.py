from django.urls import path
from .views import buscar
from .views import listar_comunas

urlpatterns = [
    path('', buscar),
    path('/comunas', listar_comunas)
]
