from django.forms import Form, CharField, TextInput, PasswordInput, ModelForm, EmailInput, FileInput, FileField, \
    IntegerField, NumberInput, Select, DateInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


from .models import Producto

class FormProducto(Form):
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
        widget=FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Imagen del producto'
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

    def save(self):
        data = self.cleaned_data
        producto = Producto()
        producto.nombre = data.get('nombre')
        producto.descripcion = data.get('descripcion')
        producto.precio = data.get('precio')
        producto.stock = data.get('stock')
        producto.imagen = data.get('imagen')
        producto.marca = data.get('marca')
        producto.save()
        return producto

    """
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise forms.ValidationError('Este producto ya existe')
        return nombre
    """