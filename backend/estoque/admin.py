from django.contrib import admin

from .models import Categoria, Produto, ProdutoEstoque


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(ProdutoEstoque)
class ProdutoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
