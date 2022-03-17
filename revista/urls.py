from django.urls import path
from . import views


app_name='revista'

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('cargarmanuscrito/', views.cargar_manuscrito, name= 'cargar_manuscrito'),
]