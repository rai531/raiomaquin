from django.urls import path
from .views import atenciones, index, contacto,login_acceso,mecanicos,servicios


urlpatterns = [

    path('atenciones',atenciones,name='atenciones'),
    path('',index,name='index'),
    path('contacto',contacto,name='contacto'),
    path('login_acceso',login_acceso,name='login_acceso'),
    path('mecanicos',mecanicos,name='mecanicos'),
    path('servicios',servicios,name='servicios'),
    





    
   
]

