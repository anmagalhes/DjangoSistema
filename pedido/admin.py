
from django.contrib import admin
from . import models

class ItempedidoInline(admin.TabularInline):
    model = models.Itempedido
    extra =1

class PedidoAdmin(admin.ModelAdmin):
    Inlines = [ItempedidoInline]

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.Itempedido)