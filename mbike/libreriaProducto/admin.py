from django.contrib import admin
from .models import Producto, Reparacion,Arriendo

# Register your models here.
admin.site.register(Producto)
admin.site.register(Arriendo)
admin.site.site_header = "Administración de MBike"
admin.site.site_title = "Administración de MBike"
admin.site.index_title = "Bienvenido a la administración de MBike"
