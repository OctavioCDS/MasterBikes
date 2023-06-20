from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm, EmailInput, NumberInput, FileInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Producto, Reparacion, Arriendo


class Registro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'class': 'form-control'}
        self.fields['password2'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class IniciarSesion(Form):
    usuario = CharField(
        required=True,
        label='Ingrese su usuario',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de Usuario'
            }
        )
    )
    contra = CharField(
        required=True,
        min_length=4,
        max_length=16,
        label='Ingrese su contraseña',
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        )
    )


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion_producto', 'precio_producto', 'stock_producto', 'imagen_producto']
        widgets = {
            'nombre_producto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Producto'
                }
            ),
            'descripcion_producto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion'
                }
            ),
            'precio_producto': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'stock_producto': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Stock'
                }
            ),
            'imagen_producto': FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'imagen'
                }
            ),

        }


class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['nombre_cliente', 'email_cliente', 'rut_cliente', 'asunto', 'descripcion',
                  'marca_bicicleta', 'modelo_bicicleta']
        widgets = {
            'nombre_cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tu nombre aquí'
                }
            ),
            'email_cliente': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email@ejemplo.com'
                }
            ),
            'rut_cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '00.000.000-0'
                }
            ),
            'asunto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cual es tu problema'
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'class': 'form-control text-area',
                    'placeholder': 'Describe con detalle el problema'
                }
            ),
            'marca_bicicleta': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'La marca de tu bicicleta'
                }
            ),
            'modelo_bicicleta': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'El modelo de tu bicicleta'
                }
            )
        }

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['nombre_cliente', 'apellido_cliente', 'rut_cliente', 'telefono_cliente', 'cantidad_dias_arriendo',
                  'fecha_inicio_arriendo', 'modelo_bicicleta', 'descripcion_de_uso']
        widgets = {
            'nombre_cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'apellido_cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido'
                }
            ),
            'rut_cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '00.000.000-0'
                }
            ),
            'telefono_cliente': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de telefono'
                }
            ),
            'cantidad_dias_arriendo': TextInput(
                attrs={
                    'class': 'form-control text-area',
                    'placeholder': 'Ingrese la cantidad de días que desea arrendar'
                }
            ),
            'fecha_inicio_arriendo': DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'marca_bicicleta': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la marca de la bicicleta'
                }
            ),
            'descripcion_de_uso': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describa el uso que dará a la bicicleta arrendada'
                }
            )
        }