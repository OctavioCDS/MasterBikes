from django.shortcuts import render,redirect
from .forms import Registro
from django.contrib.auth.forms import UserCreationForm


def principal(request):
    return render(request,'principal.html')

def mostrar_registro(request):
    contexto = {
        'titulo': 'Bienvenido',
        'formulario':Registro(),
        'registro': UserCreationForm()
    }
    return render(request,'registro.html',contexto)

def registrar_nuevo(request):
    if request.method == 'GET':
        return redirect('pagina_principal')
    if request.method == 'POST':
        formulario_registro = UserCreationForm(request.POST)
        es_valido = formulario_registro.is_valid()
        if es_valido:
            usuario_nuevo = formulario_registro.save()
            return redirect('pagina_principal')   
        contexto = {
        'titulo': 'Bienvenido',
        'formulario':Registro(),
        'registro': formulario_registro
        }
        return render(request,'registro.html',contexto)
