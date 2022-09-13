from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(default="profpic.jpg", upload_to="fotos_perfil")
    ubicacion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.username
