from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import EnderecoForm
from .models import Endereco


def endereco_list(request):
    template_name = 'endereco/endereco_list.html'
    object_list = Endereco.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class EnderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoForm
    success_url = reverse_lazy('endereco:endereco_list')
