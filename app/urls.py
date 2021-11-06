# direcciones de nuetra aplicacion

from django.urls import path
from .views import home, proveedor_view, productoView, recetaView, registro



urlpatterns = [
    path('', home, name="home"),
    path('registration/registro/',registro, name="registro"),
    path('proveedor/', proveedor_view, name= "proveedor"),
    path('producto/', productoView, name= "producto"),
    path('receta/', recetaView, name= "receta"),


    
]

