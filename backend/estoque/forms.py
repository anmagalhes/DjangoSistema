from django import forms

from .models import Categoria, Estoque, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'
