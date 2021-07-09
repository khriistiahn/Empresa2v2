from app.forms import ProductoForm, SubscripcionForm
from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descuento','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 10
    form = ProductoForm

admin.site.register(TipoPorducto)
admin.site.register(Producto, ProductoAdmin)

class SubscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fundacion']
    search_fields = ['usuario']
    list_per_page = 10
    form = SubscripcionForm

admin.site.register(Fundacion)
admin.site.register(Subscripcion, SubscripcionAdmin)