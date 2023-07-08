from django.urls import path
from .views import atenciones, index, contacto, login, mecanicos, servicios, vehiculos, agregar,agregar1,sesiones
from django.urls import include
from . import views

urlpatterns = [
    path('atenciones', atenciones, name='atenciones'),
    path('', index, name='index'),
    path('mecanicos', mecanicos, name='mecanicos'),
    path('servicios', servicios, name='servicios'),
    path('vehiculos', vehiculos, name='vehiculos'),
    path('sesiones', sesiones, name='sesiones'),
    path('agregar/', agregar, name='agregar'),
    path('agregar1/', agregar1, name='agregar1'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name="salir"),
    path('', include('paypal.urls')),
    
]

