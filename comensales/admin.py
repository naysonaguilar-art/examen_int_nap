from django.contrib import admin

# Register your models here.
from.models import Comensales
#admin.site.register(Comensales)
@admin.register(Comensales)
class Comensales(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "DNI")
    list_filter = ("nombre", "apellido", "DNI")
    search_fields = ("nombre", "apellido", "DNI")
