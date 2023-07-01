from django.shortcuts import render
from .models import Vehiculo, Categoria
from .forms import VehiculoForm


# Create your views here.

def atenciones(request):
   
    return render(request, 'atenciones.html')

def index(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,'contacto.html')

def login_acceso(request):
    return render(request,'login_acceso.html')

def mecanicos(request):
    return render(request,'mecanicos.html')

def servicios(request):
    return render(request,'servicios.html')

def vehiculos(request):
    return render(request, 'vehiculos.html')

def agregar(request):
    return render(request, 'agregar.html')








def vista_vehiculos(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'nombre':'JUAN CARLOS BODOQUEE', 'vehiculos':vVehiculos}
    return render(request, 'atenciones.html', contexto)
    
def form_vehiculo(request):
    datos = {
        'form': VehiculoForm()
    }
    if request.method== 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'atenciones.html', datos)

# def form_perrito(request):
#     datos ={
#         'form':VehiculoForm()
#         }
#     if request.method=='POST':
#         formulario = VehiculoForm(request.POST)
#         if formulario.is_valid:
#             formulario.save()
#             datos['mensaje']="Guardados correctamente"
#     return render(request, 'agregar.html',datos)




def agregar(request):
    datos ={
        'form':VehiculoForm()
        }
    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados correctamente"
    return render(request, 'agregar.html',datos)