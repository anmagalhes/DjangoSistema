from django.shortcuts import render

from .models import DocumentosRH, Funcionario, HoraExtraFuncionario


def documento_list(request):
    template_name = 'funcionario/documento_list.html'
    object_list = DocumentosRH.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def funcionario_list(request):
    template_name = 'funcionario/funcionario_list.html'
    object_list = Funcionario.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def hora_extra_list(request):
    template_name = 'funcionario/hora_extra_list.html'
    object_list = HoraExtraFuncionario.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)
