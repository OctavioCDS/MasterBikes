from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm, EmailInput, FileInput, FileField, \
    IntegerField, NumberInput, Select, DateInput, Textarea, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto


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


class Iniciar_Sesion(Form):
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


class FormProducto(Form):
    def save(self, commit=True):
        producto = Producto(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion'],
            precio=self.cleaned_data['precio'],
            stock=self.cleaned_data['stock'],
            imagen=self.cleaned_data['imagen'].read(),
            marca=self.cleaned_data['marca'],
        )

        if commit:
            producto.save()

        return producto

    nombre = CharField(
        required=True,
        label='Ingrese el nombre del producto',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }
        )
    )
    descripcion = CharField(
        required=True,
        label='Ingrese la descripcion del producto',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion del producto'
            }
        )
    )
    precio = IntegerField(
        required=True,
        label='Ingrese el precio del producto',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Precio del producto'
            }
        )
    )
    stock = IntegerField(
        required=True,
        label='Ingrese el stock del producto',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Stock del producto'
            }
        )
    )
    imagen = FileField(
        required=True,
        label='Ingrese la imagen del producto',
        widget=ClearableFileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Imagen del producto',
            }
        )
    )

    marca = CharField(
        required=True,
        label='Ingrese la marca del producto',
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Marca del producto'
            }
        )
    )

