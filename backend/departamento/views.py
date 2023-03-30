from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import DepartamentoForm
from .models import Departamento


def departamento_list(request):
    template_name = 'departamento/departamento_list.html'
    object_list = Departamento.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento:departamento_list')


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamento:departamento_list')
