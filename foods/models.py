from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Alimento(models.Model):
    def __str__(self) -> str:
        return self.nombre_alimento

    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre_alimento = models.CharField(max_length=200)
    desc_alimento = models.CharField(max_length=200)
    precio_alimento = models.IntegerField()
    imagen_alimento = models.CharField(
        max_length=500,
        default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5PTsuRj6pjDdRDNqaC27k705rxveiomd99w&usqp=CAU",
    )

    def get_absolute_url(self):
        return reverse("foods:detalles", kwargs={"pk": self.pk})
