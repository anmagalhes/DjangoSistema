from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CategoriaForm, EstoqueForm, ProdutoForm
from .models import Categoria, Estoque, Produto


def categoria_list(request):
    template_name = 'estoque/categoria_list.html'
    object_list = Categoria.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def estoque_list(request):
    template_name = 'estoque/estoque_list.html'
    object_list = Estoque.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def produto_list(request):
    template_name = 'estoque/produto_list.html'
    object_list = Produto.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('estoque:categoria_list')


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('estoque:estoque_list')


class EstoqueCreateView(CreateView):
    model = Estoque
    form_class = EstoqueForm
    success_url = reverse_lazy('estoque:produto_list')
