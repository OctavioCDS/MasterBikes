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
from .views import mostrar_registro, Principal,Mantenciones,Producto, iniciar_sesion, mostrar_iniciar_sesion

urlpatterns = [
    path('Principal',Principal,name='Principal'),
    path('Mantenciones/',Mantenciones,name='Mantenciones'),
    path('Producto/',Producto,name='Producto'),
    path('mostrar_registro',mostrar_registro,name='mostrar_registro'),
    path('admin/', admin.site.urls),
    path('iniciar/',iniciar_sesion,name='iniciar_sesion'),
<<<<<<< HEAD
    path('sesion/',mostrar_iniciar_sesion,name='iniciar_sesion_user'),
=======
    path('mostrar_iniciar_sesion/',mostrar_iniciar_sesion,name='mostrar_iniciar_sesion'),
>>>>>>> d6ff79fb3f91cc3cd8b4d2b15d0f5ecef2a8a08d
]
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
