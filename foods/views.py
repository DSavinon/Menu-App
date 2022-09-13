from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from foods.forms import AlimentoForm

from .models import Alimento

# Create your views here.


class IndexClassView(ListView):
    model = Alimento
    template_name = "foods/index.html"
    context_object_name = "lista_alimentos"


class DetallesClassView(DetailView):
    model = Alimento
    template_name = "foods/detalles.html"
    context_object_name = "detalles_alimentos"


# def index(request):
#    lista_alimentos = Alimento.objects.all()
#    index_context = {"lista_alimentos": lista_alimentos}
#    return render(request, "foods/index.html", index_context)


# def detalles(request, alimento_id):
#    detalles_alimentos = Alimento.objects.get(pk=alimento_id)
#    detalles_context = {"detalles_alimentos": detalles_alimentos}
#    return render(request, "foods/detalles.html", detalles_context)


# def agregar_alimento(request):
#   form = AlimentoForm(request.POST or None)
#  agregar_context = {"form": form}

# if form.is_valid():
#    form.save()
#   return redirect("foods:index")
# return render(request, "foods/agregar-form.html", agregar_context)


class AgregarAlimento(CreateView):
    model = Alimento
    fields = ["nombre_alimento", "desc_alimento", "precio_alimento", "imagen_alimento"]
    template_name = "foods/agregar-form.html"

    def form_valid(self, form):
        form.instance.nombre_usuario = self.request.user
        return super().form_valid(form)


def editar_alimento(request, alimento_id):
    alimento = Alimento.objects.get(pk=alimento_id)
    form = AlimentoForm(request.POST or None, instance=alimento)
    edit_context = {"alimento": alimento, "form": form}

    if form.is_valid():
        form.save()
        return redirect("foods:index")
    return render(request, "foods/agregar-form.html", edit_context)


def borrar_alimento(request, alimento_id):
    alimento = Alimento.objects.get(pk=alimento_id)
    borrar_context = {"alimento": alimento}

    if request.method == "POST":
        alimento.delete()
        return redirect("foods:index")
    return render(request, "foods/borrar-form.html", borrar_context)
