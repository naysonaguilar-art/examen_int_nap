from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"




    class Meta:
        verbose_name = "Plato"  # Nombre en singular
        verbose_name_plural = "Platos"  # Nombre en plural (esto quita la doble S)