from django.shortcuts import render

from .models import Endereco


def endereco_list(request):
    template_name = 'endereco/endereco_list.html'
    object_list = Endereco.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
