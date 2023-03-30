from django.shortcuts import render

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
