from django.db import models

from comensales.models import Comensales

# Create your models here.
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    comensales = models.ForeignKey(Comensales, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comensales},"

