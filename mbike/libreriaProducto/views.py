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


def formularios(request):
    return render(request, 'formularios.html')


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

def arriendo(request):
    return render(request, 'Arriendo.html')


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


# Funciones - Formulario de reparacion

def guardar_formulario_reparacion(request):
    if request.method == 'POST':
        formulario = ReparacionForm(request.POST)
        print(formulario)
        print('Form reparacion')
        if formulario.is_valid():
            print('Valid')
            formulario.save()
            success(request, 'Se ha enviado su solicitud')
            return redirect('Cliente')
        else:
            print('form not valid')
    else:
        print('not a post request')
        formulario = ReparacionForm()
    print('end form')
    return render(request, 'Cliente.html', {'formulario': formulario})


def eliminar_solicitud_reparacion(request, id):
    reparacion = Reparacion.objects.get(id=id)
    reparacion.delete()
    success(request, 'Se elimino su solicitud')
    return redirect("Cliente")


def buscar_solicitud_reparacion(request):
    if request.method == 'POST':
        rut_cliente = request.POST.get('rut_cliente')

        reparacion = Reparacion.objects.filter(rut_cliente=rut_cliente)

        return render(request, 'Cliente.html', {'reparacion': reparacion})

    return render(request, 'Cliente.html')

# Arriendo

def guardar_arriendo(request):
    if request.method == 'POST':
        formulario_arriendo = ArriendoForm(request.POST)
        print(formulario_arriendo)
        print('Form reparacion')
        if formulario_arriendo.is_valid():
            print('Valid')
            formulario_arriendo.save()
            success(request, 'Se ha enviado su solicitud')
            return redirect('Arriendo')
        else:
            print('form not valid')
    else:
        print('not a post request')
        formulario_arriendo = ArriendoForm()
    print('end form')
    return render(request, 'Arriendo.html', {'formulario_arriendo': formulario_arriendo})
def LReparaciones(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'ListaReparaciones.html', {'reparaciones': reparaciones})