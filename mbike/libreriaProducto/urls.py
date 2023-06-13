"""
URL configuration for mbike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', Principal, name='Principal'),
    path('Mantenciones/', Mantenciones, name='Mantenciones'),
    # Tienda
    # path('Tienda_articulos/',Tienda_articulos,name='Tienda_articulos'),
    path('Tienda_bicicletas/', tienda_bicicletas, name='Tienda_bicicletas'),
    # path('Tienda_ropa/',Tienda_ropa,name='Tienda_ropa'),
    # Fin tienda
    path('mostrar_registro', mostrar_registro, name='mostrar_registro'),
    path('admin/', admin.site.urls),
    path('mostrar_iniciar_sesion/', mostrar_iniciar_sesion, name='mostrar_iniciar_sesion'),
    path('salir/', cerrar_sesion, name='cerrar_sesion'),
    path('contacto/', formulario_contacto, name='formulario_contacto'),
    path('privacidad/', privacidad, name='privacidad'),
    path('tiendas/', tiendas_fisicas, name='tiendas_fisicas'),
    path('Agregar/', AgregarProducto , name="Agregar" ),
    path('Modificar/<id>', ModificarProducto, name="Modificar"),
    path('Eliminar', EliminarProducto, name="Eliminar"),
    path('Vendedor/', Vendedor, name='Vendedor'),
    path('BuscarProducto/', BuscarProducto, name="BuscarProducto"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)