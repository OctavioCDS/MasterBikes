from django.contrib import admin
from .models import Producto, Reparacion

# Register your models here.
admin.site.register(Producto)
admin.site.site_header = "Administración de MBike"
admin.site.site_title = "Administración de MBike"
admin.site.index_title = "Bienvenido a la administración de MBike"
