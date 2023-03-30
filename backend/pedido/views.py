from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PedidoForm
from .models import Pedido


def pedido_list(request):
    template_name = 'pedido/pedido_list.html'
    object_list = Pedido.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedido:pedido_list')
