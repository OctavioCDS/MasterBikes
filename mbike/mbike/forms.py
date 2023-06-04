from django.forms import TextInput

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