from django.forms import TextInput, PasswordInput, ModelForm,EmailInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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