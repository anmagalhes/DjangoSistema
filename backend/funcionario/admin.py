from django.contrib import admin

from .models import DocumentosRH, Funcionario, HoraExtraFuncionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(DocumentosRH)
class DocumentosRHAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(HoraExtraFuncionario)
class HoraExtraFuncionarioAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
