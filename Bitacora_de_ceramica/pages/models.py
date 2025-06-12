from django.db import models
from ckeditor.fields import RichTextField

class Pieza(models.Model):
    titulo = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='piezas/')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


