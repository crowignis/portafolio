# direcciones de nuetra aplicacion

from django.urls import path
from .views import home, inicio, registro1, proveedor_view



urlpatterns = [
    path('', home, name="home"),
    path('inicio/', inicio, name="inicio"),
    path('registro1/', registro1, name="registro1"),
    path('proveedor/', proveedor_view, name= "proveedor"),


    

    
    
]

