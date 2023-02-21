from django.shortcuts import render, redirect
from cliente.models import *
from cliente.forms import *
import datetime

def cadastrar_cliente(request):
    form = ClienteForm()

    if request.method == "POST":
        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_cliente")

    context = {

        "nome_pagina": "Cadastrar Cliente",
        "form": form
    }

    return render(request, "cadastrar_cliente.html", context)
