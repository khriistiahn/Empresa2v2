from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import Permission, User

# Create your models here.

class TipoPorducto(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=40)
    tipo = models.ForeignKey(TipoPorducto, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(null =True, blank=True)
    descuento = models.IntegerField()

    def __str__(self):
        return self.nombre

class Fundacion(models.Model):
    fundacion = models.CharField(max_length=40)
    monto_sub = models.IntegerField()
    descuento = models.IntegerField()
    def __str__(self):
        return self.fundacion

class Subscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario

#python manage.py makemigrations --- CREA EL ARCHIVO PARA MIGRAR
#python manage.py migrate --- ENVIA EL ARCHIVO A LA BD
#python manage.py createsuperuser --- CREA EL ADMIN EN LA WEB

"""
odd_even = Permission.objects.get(name='can_view_even_ids')
user_yui = User.objects.get(username='yui')
user_yui.user_permissions.add(odd_even)
user_yui.save()
"""