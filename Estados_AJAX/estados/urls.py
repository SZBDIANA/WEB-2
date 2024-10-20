from django.urls import path
from . import views

urlpatterns = [
    path('', views.estados_municipios_view, name='estados_municipios'),
    path('cargar-municipios/', views.cargar_municipios, name='cargar_municipios'),
]
