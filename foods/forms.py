from django import forms

from .models import Alimento


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = [
            "nombre_alimento",
            "desc_alimento",
            "precio_alimento",
            "imagen_alimento",
        ]
