from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("registrarse", views.registrarse, name="registrarse"),
    path("perfil", views.perfil_usuario, name="perfil"),
]
