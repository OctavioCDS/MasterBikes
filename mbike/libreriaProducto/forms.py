from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm,EmailInput,NumberInput,FileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Producto

class Registro(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = {'class':'form-control'}
        self.fields['password2'].widget.attrs = {'class':'form-control'}
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email']
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'last_name': TextInput(
                attrs ={
                    'class':'form-control'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }

class Iniciar_Sesion(Form):
    usuario = CharField(
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Nombre de Usuario'
            }
        )
    )
    contra = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Contraseña'
            }
        )
    )

class ProductoForm(forms.ModelForm):

    class Meta:
       model = Producto
       fields = ['nombre_producto', 'descripcion_producto','precio_producto','stock_producto','imagen_producto']
       widgets = {
            'nombre_producto': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Nombre Producto'
                }
            ),
            'descripcion_producto': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Descripcion'
                }
            ),
            'precio_producto': NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Precio'
                }
            ),
            'stock_producto': NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Stock'
                }
            ),
            'imagen_producto': FileInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'imagen'
                }
            ),

        }