from cliente.models import *
from django import forms


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
