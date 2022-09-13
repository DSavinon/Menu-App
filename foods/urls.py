from django.urls import path

from . import views

app_name = "foods"

urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path("<int:pk>/", views.DetallesClassView.as_view(), name="detalles"),
    path("agregar/", views.AgregarAlimento.as_view(), name="agregar_alimento"),
    path("editar/<int:alimento_id>/", views.editar_alimento, name="editar_alimento"),
    path("borrar/<int:alimento_id>", views.borrar_alimento, name="borrar_alimento"),
]
