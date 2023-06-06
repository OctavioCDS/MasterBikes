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
            es_valido = formulario_registro.is_valid() # Retorna un bool
            if es_valido: # Si bool es True
                usuario_nuevo = formulario_registro.save()
                success(request,'Gracias por registrarse con nosotros :D')
                return redirect('Principal')
            contexto = {
                'formulario': formulario_registro
            }
            warning(request,'Ups... ha ocurrido un error en la insercion de datos')
            return render(request,'registro.html',contexto)

def mostrar_iniciar_sesion(request):
    contexto = {
        'titulo': 'Bienvenido, inicie sesión',
        'formulario_sesion':Iniciar_Sesion()
    }
    return render(request,'iniciar_sesion.html',contexto)

def iniciar_sesion (request):
    if request.method == 'GET':
        return redirect('principal.html')
    if request.method == 'POST':
        contexto = {
        'titulo': 'Bienvenido, inicie sesión',
        'formulario_sesion':Iniciar_Sesion()
        }  
        form = Iniciar_Sesion(request.POST)
        if form.is_valid():
            usuario = request.POST["username"]
            contrasenia = request.POST["password"]
            usuar = authenticate(request, usuario=usuario, contrasenia=contrasenia)
            if usuar is not None:
                login(request, usuar)
<<<<<<< HEAD
                success(request,'Sesión iniciada con éxito')
                return redirect('pagina_principal')
=======
                return redirect('principal.html')
>>>>>>> d6ff79fb3f91cc3cd8b4d2b15d0f5ecef2a8a08d
            else:
                return render(request, "principal.html")
        else:
            form.add_error(None, 'Credenciales inválidas')
            return render(request, "principal.html")

def desconectarse(request):
    logout(request)
    return redirect('principal.html')