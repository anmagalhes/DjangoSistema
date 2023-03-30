from django import forms

from .models import Documento, Funcionario, HoraExtraFuncionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'


class HoraExtraFuncionarioForm(forms.ModelForm):
    class Meta:
        model = HoraExtraFuncionario
        fields = '__all__'
