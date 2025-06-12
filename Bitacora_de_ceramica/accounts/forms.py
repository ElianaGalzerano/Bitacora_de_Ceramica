from django import forms
from accounts.models import Perfil, Pieza
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio', 'fecha_nacimiento', 'link']

class PiezaForm(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['titulo', 'descripcion', 'imagen']

