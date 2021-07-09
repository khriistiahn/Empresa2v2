from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields
from .models import Producto, Subscripcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User
from .validators import TamanioMaximoValidator
from django.contrib.auth import authenticate

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=5,max_length=30)
    precio = forms.IntegerField(min_value=5000)
    descripcion = forms.CharField(min_length=10,max_length=100)
    imagen = forms.ImageField(validators=[TamanioMaximoValidator(maxfile=1)],required=False)
    descuento = forms.IntegerField(min_value=0, max_value=75)

    def clean_nombre(self):
        nom = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nom).exists()

        if existe:
            raise ValidationError("Este juego ya existe!")
        return nom

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descuento', 'descripcion', 'tipo', 'fecha', 'imagen']
        widgets = {
            'fecha' : forms.SelectDateWidget(years=range(2000,2030))
        }

class SubscripcionForm(ModelForm):
    class Meta:
        model = Subscripcion
        fields = ['fundacion']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
