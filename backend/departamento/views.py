from django.shortcuts import render

from .models import Departamento


def departamento_list(request):
    template_name = 'departamento/departamento_list.html'
    object_list = Departamento.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
