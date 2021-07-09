from django.forms import ValidationError
from django.db.models import fields
from rest_framework import serializers
from .models import Producto, TipoPorducto, Fundacion, Subscripcion
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

class TipoProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoPorducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    

    class Meta:
        model = Producto
        fields = '__all__'

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise ValidationError("Este producto ya existe!")

    def validate_precio(self, value):
        if value < 5000:
            raise ValidationError("El precio no puede ser menor a 5000")
        return value

#SUBCRIPCION API
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundacion
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    fundacion = FundacionSerializer(read_only=True)

    class Meta:
        model = Subscripcion
        fields = '__all__'