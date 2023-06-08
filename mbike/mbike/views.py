from django.shortcuts import render, redirect
from .forms import Registro, Iniciar_Sesion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from sweetify import info, success, warning, error


def Principal(request):
    return render(request, 'principal.html')


def Mantenciones(request):
    return render(request, 'Mantenciones.html')


# tiendas
# def Tienda_ropa(request):
#    return render(request,'Tienda_ropa.html')

# def Tienda_articulos(request):
#    return render(request,'Tienda_articulos.html')

def Tienda_bicicletas(request):
    return render(request, 'Tienda_bicicletas.html')


def formulario_contacto(request):
    return render(request, 'formulario_contacto.html')


def privacidad(request):
    return render(request, 'privacidad.html')


def tiendas_fisicas(request):
    return render(request, 'tiendas_fisicas.html')


# fin tiendas

def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': Registro()
        }
        return render(request, 'registro.html', contexto)
    if request.method == 'POST':
        formulario_registro = Registro(data=request.POST)
        es_valido = formulario_registro.is_valid()
        if es_valido:
            usuario_nuevo = formulario_registro.save()
            success(request, 'Gracias por registrarse con nosotros :D')
            return redirect('Principal')
        contexto = {
            'formulario': formulario_registro
        }
        warning(request, 'Ups... ha ocurrido un error en la insercion de datos')
        return render(request, 'registro.html', contexto)


def mostrar_iniciar_sesion(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario_sesion': Iniciar_Sesion()
        }
        return render(request, 'iniciar_sesion.html', contexto)
    if request.method == 'POST':
        datos_usuario = Iniciar_Sesion(data=request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username=datos_usuario.cleaned_data['usuario'],
                password=datos_usuario.cleaned_data['contra']
            )
            if usuario is not None:
                login(request, usuario)
                success(request, f'Inicio de sesión correcto, bienvenido {usuario.username}')
                return redirect('Principal')
        warning(request, 'Usuario y contraseña invalidos')
        contexto = {
            'formulario_sesion': datos_usuario
        }
        return render(request, 'iniciar_sesion.html', contexto)


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesión cerrada')
    return redirect('Principal')
