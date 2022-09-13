from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistrarseForm


# Create your views here.
def registrarse(request):
    if request.method == "POST":
        form = RegistrarseForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get("username")
            messages.success(
                request, f"Bienvenido {usuario}, tu cuenta ha sido registrada."
            )
            return redirect("login")
    else:
        form = RegistrarseForm()
    reg_context = {"form": form}
    return render(request, "users/registrarse.html", reg_context)


@login_required
def perfil_usuario(request):
    return render(request, "users/perfil.html")
