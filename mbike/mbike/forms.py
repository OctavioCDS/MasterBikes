from django.forms import TextInput, PasswordInput, ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class Iniciar_Sesion(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'password': PasswordInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }
        error_messages = {
            "msg": {
                "max_length": ("Error we haces todo mal"),
            },
        }