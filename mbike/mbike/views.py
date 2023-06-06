from django.shortcuts import render,redirect
from .forms import Registro, Iniciar_Sesion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from sweetify import info,success,warning,error

def Principal(request):
    return render(request,'principal.html')

def Mantenciones(request):
    
    return render(request,'Mantenciones.html')

def Producto(request):
    return render(request,'Producto.html')



def mostrar_registro(request):
        if request.method == 'GET':
            contexto = {
                'formulario': Registro()
            }
            return render(request,'registro.html',contexto)
        if request.method == 'POST':
            formulario_registro = Registro(data=request.POST)
            es_valido = formulario_registro.is_valid()
            if es_valido:
                usuario_nuevo = formulario_registro.save()
                success(request,'Gracias por registrarse con nosotros :D')
                return redirect('Principal')
            contexto = {
                'formulario': formulario_registro
            }
            warning(request,'Ups... ha ocurrido un error en la insercion de datos')
            return render(request,'registro.html',contexto)

def mostrar_iniciar_sesion (request):
    if request.method == 'GET':
            contexto = {
                'formulario_sesion':Iniciar_Sesion()
            }
            return render(request,'iniciar_sesion.html',contexto)
    if request.method == 'POST':
        form = Iniciar_Sesion(data=request.POST)
        user = request.POST["username"]
        contra = request.POST["password"]
        usuario = authenticate(request, username=user, password=contra)
        if usuario is not None:
            success(request,f'Sesión iniciada con éxito, bienvenid@ {user}')
            login(request, usuario)
            return redirect('Principal')
        else:
            warning(request,'Error en los datos ingresados, re-intentar')
            return redirect('mostrar_iniciar_sesion')

def desconectarse(request):
    logout(request)
    success(request,'Sesión cerrada con éxito')
    return redirect('principal.html')