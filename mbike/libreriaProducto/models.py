from typing import Any, Dict, Tuple
from django.db import models


class Producto(models.Model):
    nombre_producto = models.TextField()
    descripcion_producto = models.TextField()
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        hola = "Nombre: " + self.nombre_producto + " - " + "Descripcion: " + self.descripcion_producto
        return hola
