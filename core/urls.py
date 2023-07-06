from django.urls import path
from .views import atenciones,index,contacto,login,mecanicos,servicios,vehiculos,agregar
from django.urls import include
from . import views




urlpatterns = [

    path('atenciones',atenciones,name='atenciones'),
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('mecanicos',mecanicos,name='mecanicos'),
    path('servicios',servicios,name='servicios'),
    path('vehiculos',vehiculos,name='vehiculos'),
    path('agregar/',agregar,name='agregar'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('salir/' , views.salir, name="salir" )

  
]

