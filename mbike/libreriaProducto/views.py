from django.shortcuts import render, redirect
from .forms import Registro, IniciarSesion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from sweetify import info, success, warning, error
from .models import Producto, Reparacion
from .forms import ProductoForm, ReparacionForm


def principal(request):
    return render(request, 'principal.html')


def mantenciones(request):
    return render(request, 'Mantenciones.html')


# tiendas
# def Tienda_ropa(request):
#    return render(request,'Tienda_ropa.html')

# def Tienda_articulos(request):
#    return render(request,'Tienda_articulos.html')

def tienda_bicicletas(request):
    return render(request, 'Tienda_bicicletas.html')


def formulario_contacto(request):
    return render(request, 'formulario_contacto.html')


def privacidad(request):
    return render(request, 'privacidad.html')


def tiendas_fisicas(request):
    return render(request, 'tiendas_fisicas.html')


def vendedor(request):
    productos = Producto.objects.all()
    return render(request, 'Vendedor.html', {'productos': productos})


def reparaciones(request):
    solicitudes = Reparacion.objects.all()
    return render(request, 'Reparaciones.html', {'reparaciones': solicitudes})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success(request, 'El producto se ha agreado correctamente :D')
            # Realizar cualquier otra acción necesaria, como mostrar un mensaje de éxito o redireccionar a otra página
            return redirect('Vendedor')
    else:
        form = ProductoForm()

    contexto = {'form': form}
    return render(request, 'Vendedor.html', contexto)


def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    contexto = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == "POST":
        form = ProductoForm(data=request.POST, instance=producto)
        if form.is_valid():
            form.save()
            success(request, 'El producto se ha modificado correctamende:D')
        productos = Producto.objects.all()
        return render(request, 'Vendedor.html', {'productos': productos})
    return render(request, 'Modificar.html', contexto)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    success(request, 'Producto Eliminado correctamente.. :D')
    return redirect("Vendedor")


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
            'formulario_sesion': IniciarSesion()
        }
        return render(request, 'iniciar_sesion.html', contexto)
    if request.method == 'POST':
        datos_usuario = IniciarSesion(data=request.POST)
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


def buscar_producto(request):
    productos = Producto.objects.filter(nombre_producto=request.POST["nombre_producto"])
    return render(request, 'Vendedor.html', {'productos': productos})


def guardar_formulario_reparacion(request):
    if request.method == 'POST':
        formulario = ReparacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Se ha guardado su solicitud')
            return redirect('Principal')
    else:
        formulario = ReparacionForm()
    return render(request, 'Cliente.html', {'formulario': formulario})

