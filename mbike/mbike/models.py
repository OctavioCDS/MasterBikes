from django.db import models


class Producto(models.Model):
    class Meta:
        app_label = 'mbike'

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.BinaryField()
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

