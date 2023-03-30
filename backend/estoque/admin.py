from django.contrib import admin

from .models import Categoria, Estoque, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
