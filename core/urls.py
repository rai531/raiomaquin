from django.urls import path
from .views import atenciones, index, contacto,login_acceso,mecanicos,servicios,vehiculos,agregar




urlpatterns = [

    path('atenciones',atenciones,name='atenciones'),
    path('',index,name='index'),
    path('login_acceso',login_acceso,name='login_acceso'),
    path('mecanicos',mecanicos,name='mecanicos'),
    path('servicios',servicios,name='servicios'),
    path('vehiculos',vehiculos,name='vehiculos'),
    path('agregar',agregar,name='agregar')
  
]

