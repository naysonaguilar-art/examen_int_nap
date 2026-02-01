from django.db import models

# Create your models here.
class Comensales(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellido = models.CharField(max_length=200, null=True, blank=True)
    DNI = models.CharField(max_length=200, default='00000000')

    def __str__(self):
        return f"{self.nombre}"




    class Meta:
        verbose_name = "Comensal"  # Nombre en singular
        verbose_name_plural = "Comensales"  # Nombre en plural (esto quita la doble S)
