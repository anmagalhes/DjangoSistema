from django.shortcuts import render
from .models import Fornecedor


def fornecedor_list(request):
    template_name = 'fornecedor/fornecedor_list.html'
    object_list = Fornecedor.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
