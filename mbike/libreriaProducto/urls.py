from django.urls import path
from django.conf import settings
from .views import *
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('', principal, name='Principal'),
                  path('Mantenciones/', mantenciones, name='Mantenciones'),
                  # Tienda
                  # path('Tienda_articulos/',Tienda_articulos,name='Tienda_articulos'),
                  path('Tienda_bicicletas/', tienda_bicicletas, name='Tienda_bicicletas'),
                  # path('Tienda_ropa/',Tienda_ropa,name='Tienda_ropa'),
                  # Fin tienda
                  path('mostrar_registro', mostrar_registro, name='mostrar_registro'),
                  path('mostrar_iniciar_sesion/', mostrar_iniciar_sesion, name='mostrar_iniciar_sesion'),
                  path('salir/', cerrar_sesion, name='cerrar_sesion'),
                  path('contacto/', formulario_contacto, name='formulario_contacto'),
                  path('privacidad/', privacidad, name='privacidad'),
                  path('tiendas/', tiendas_fisicas, name='tiendas_fisicas'),
                  path('Agregar/', agregar_producto, name="Agregar"),
                  path('Modificar/<id>', modificar_producto, name="Modificar"),
                  path('Eliminar/<id>', eliminar_producto, name="Eliminar"),
                  path('Vendedor/', vendedor, name='Vendedor'),
                  path('BuscarProducto/', buscar_producto, name="BuscarProducto"),
                  path('Cliente', guardar_formulario_reparacion, name='Cliente'),
                  path('Reparaciones', reparaciones, name='Reparaciones'),
                  path('Arriendo', arriendo, name='Arriendo'),
                  path('formularios', formularios, name='Formularios'),
                  path('EliminarReparacion/<id>', eliminar_solicitud_reparacion, name="EliminarReparacion"),
                  path('BuscarReparacion/', buscar_solicitud_reparacion, name="BuscarReparacion"),
                  path('LReparaciones/', LReparaciones, name="LReparaciones"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
