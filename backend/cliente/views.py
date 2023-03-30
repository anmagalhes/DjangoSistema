from django.shortcuts import render
from .models import Cliente


def cliente_list(request):
    template_name = 'cliente/cliente_list.html'
    object_list = Cliente.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
