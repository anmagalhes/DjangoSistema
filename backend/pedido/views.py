from django.shortcuts import render

from .models import Pedido


def pedido_list(request):
    template_name = 'pedido/pedido_list.html'
    object_list = Pedido.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
