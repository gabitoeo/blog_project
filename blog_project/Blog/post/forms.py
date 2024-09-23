from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None 
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 8 caracteres.'
        self.fields['password2'].help_text = 'Ingresa la misma contraseña para confirmarla.'
