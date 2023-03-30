from django.contrib import admin

from .models import Itempedido, Pedido


class ItempedidoInline(admin.TabularInline):
    model = Itempedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    Inlines = [ItempedidoInline]
    list_display = ('__str__',)
