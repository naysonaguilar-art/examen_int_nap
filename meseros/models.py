from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    nacionalidad = models.CharField(max_length=200, null=True, blank=True)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"




    class Meta:
        verbose_name = "Mesero"  # Nombre en singular
        verbose_name_plural = "Meseros"  # Nombre en plural (esto quita la doble S)