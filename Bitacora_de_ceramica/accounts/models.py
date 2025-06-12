from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)

 
    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"

    

