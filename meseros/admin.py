from django.contrib import admin

# Register your models here.
from .models import Meseros
#admin.site.register(Meseros)
@admin.register(Meseros)
class Meseros(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad", "edad")
    list_filter = ("nombre", "nacionalidad", "edad")
    search_fields = ("nombre", "nacionalidad", "edad")
