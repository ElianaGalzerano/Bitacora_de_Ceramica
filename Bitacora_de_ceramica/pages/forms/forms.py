from django import forms
from pages.models import Pieza

class PiezaForm(forms.ModelForm):
    class Meta:
        model = Pieza
        fields = ['titulo', 'tecnica', 'descripcion', 'imagen']
