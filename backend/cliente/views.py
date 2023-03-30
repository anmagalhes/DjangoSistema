from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ClienteForm
from .models import Cliente


def cliente_list(request):
    template_name = 'cliente/cliente_list.html'
    object_list = Cliente.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:cliente_list')
