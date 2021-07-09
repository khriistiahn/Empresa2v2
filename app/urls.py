from django.urls import path, include
from .views import *
from rest_framework import routers

#todas las rutas del CRUD
#URL: api/producto
router = routers.DefaultRouter()
router.register('Producto', ProductoViewSet)
router.register('subscripcion', SubscripcionViewSet)

from  .views import agregar, modificar, eliminar, tabla

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
    path('ingreso/', ingreso, name="ingreso"),
    path('registro/', registro, name="registro"),

    #Admin
    path('agregar/', agregar, name="agregar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('tabla/', tabla, name="tabla"),

    #registrarse
    path('registraruser/', registrar_user, name="registrar_user"),
    path('subscripcion/', subscripsion, name="subscripcion"),
    path('eliminar_sub/<id>/', eliminar_sub, name='eliminar_sub'),

    path('api/', include(router.urls))
]