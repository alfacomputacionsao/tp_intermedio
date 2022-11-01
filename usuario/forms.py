from dataclasses import fields
from django. forms import ModelForm
from .models import Panel_Cliente

class form_cliente (ModelForm):
    class Meta:
        model = Panel_Cliente
        fields = ['nombre', 'direccion', 'dni', 'email']