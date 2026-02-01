from django.contrib import admin

# Register your models here.
from.models import Pedido
#admin.site.register(Pedido)
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("fecha", "comensales")
    list_filter = ("fecha", "comensales")
    search_fields = ("fecha", "comensales")