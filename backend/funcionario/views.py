from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import DocumentoForm, FuncionarioForm, HoraExtraFuncionarioForm
from .models import Documento, Funcionario, HoraExtraFuncionario


def documento_list(request):
    template_name = 'funcionario/documento_list.html'
    object_list = Documento.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class DocumentoCreateView(CreateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('funcionario:funcionario_list')


class DocumentoUpdateView(UpdateView):
    model = Documento
    form_class = DocumentoForm
    success_url = reverse_lazy('funcionario:funcionario_list')


def funcionario_list(request):
    template_name = 'funcionario/funcionario_list.html'
    object_list = Funcionario.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('funcionario:documento_list')


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('funcionario:documento_list')


def hora_extra_list(request):
    template_name = 'funcionario/horaextrafuncionario_list.html'
    object_list = HoraExtraFuncionario.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


class HoraExtraFuncionarioCreateView(CreateView):
    model = HoraExtraFuncionario
    form_class = HoraExtraFuncionarioForm
    success_url = reverse_lazy('funcionario:hora_extra_list')


class HoraExtraFuncionarioUpdateView(UpdateView):
    model = HoraExtraFuncionario
    form_class = HoraExtraFuncionarioForm
    success_url = reverse_lazy('funcionario:hora_extra_list')
