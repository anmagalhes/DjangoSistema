from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FornecedorForm
from .models import Fornecedor


def fornecedor_list(request):
    template_name = 'fornecedor/fornecedor_list.html'
    object_list = Fornecedor.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    success_url = reverse_lazy('fornecedor:fornecedor_list')
