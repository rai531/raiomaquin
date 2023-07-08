from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Vehiculo, Categoria
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login



# Create your views here.


def atenciones(request):
   
    return render(request, 'atenciones.html')

def index(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,'contacto.html')

@login_required
def sesiones(request):
    return render(request,'sesiones.html')


def mecanicos(request):
    return render(request,'mecanicos.html')

def servicios(request):
    return render(request,'servicios.html')

def vehiculos(request):
    return render(request, 'vehiculos.html')


def agregar1(request):
     if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos han sido guardados con éxito.')
            return render(request, 'index.html')
        
        


def salir(request):
    logout(request)
    return redirect('/')



def atenciones(request):
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