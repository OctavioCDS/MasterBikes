from django.db import models


# Crea el modelo producto


class Producto(models.Model):

    class meta:
        app_label = 'mbike'

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.BinaryField()

    def __str__(self):
        return self.nombre

