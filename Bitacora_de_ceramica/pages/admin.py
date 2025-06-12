from django.contrib import admin
from .models import Pieza

@admin.register(Pieza)
class PiezaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tecnica', 'descripcion', 'imagen']