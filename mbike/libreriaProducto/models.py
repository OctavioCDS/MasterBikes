from typing import Any, Dict, Tuple
from django.db import models


class Producto(models.Model):
    nombre_producto = models.TextField()
    descripcion_producto = models.TextField()
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        detalle = "Nombre: " + str(self.nombre_producto) + " - " + "Descripcion: " + str(self.descripcion_producto)
        return detalle


class Reparacion(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    email_cliente = models.EmailField()
    rut_cliente = models.CharField(max_length=9)
    asunto = models.CharField(max_length=150)
    descripcion = models.TextField()
    marca_bicicleta = models.CharField(max_length=100)
    modelo_bicicleta = models.CharField(max_length=150)
    # fecha_ingreso = models.DateField()

    def __str__(self):
        detalle = "Nombre: " + str(self.nombre_cliente) + ", " + "Asunto: " + str(self.asunto)
        return detalle

class Arriendo(models.Model):
    nombre_cliente = models.CharField(max_length=200,null = False)
    apellido_cliente = models.CharField(max_length=200,null = False)
    rut_cliente = models.CharField(max_length=10,null = False)
    telefono_cliente = models.CharField(max_length=9, null = False)
    cantidad_dias_arriendo = models.IntegerField(null = False)
    fecha_inicio_arriendo = models.DateField(auto_now_add = True)
    modelo_bicicleta = models.CharField(max_length=150,null = False)
    descripcion_de_uso = models.TextField(null = False)