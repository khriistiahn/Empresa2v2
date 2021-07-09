from django.contrib.auth import authenticate, login
from django.core import paginator
from django.shortcuts import redirect, render
from .models import Producto, Subscripcion
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, SubscriptionSerializer

#Admin
from .forms import ProductoForm, SubscripcionForm, CustomUserCreationForm
from django.contrib.auth.models import Permission, User

# Create your views here.

# VISTA PARA LEVANTAR EL INDEX
def index(request):
    return render(request, 'app/index.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def productos(request):
    productoAll = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productoAll, 5)
        productoAll = paginator.page(page)
    except:
        raise Http404

    datos = {
        'lista' : productoAll, 'paginator' : paginator
    }
    datos['tipo'] = list(Producto.objects.values_list())

    return render(request, 'app/productos.html', datos)

def ingreso(request):
    return render(request, 'app/ingreso.html')

def registro(request):
    return render(request, 'app/registro.html')

#ADMIN
@permission_required('app.add_producto')
def agregar(request):
    datos = {
        'formulario' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto Agregado'
        
        datos['formulario'] = formulario
        return redirect(to='tabla')

    return render(request, 'app/admin/agregar.html', datos)


@permission_required('app.change_producto')
def modificar(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'formulario' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files= request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto Modificado'
            datos['formulario'] = formulario

    return render(request, 'app/admin/modificar.html', datos)

@permission_required('app.delete_producto')
def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to='tabla')

@permission_required('app.view_producto')
def tabla(request):
    productoAll = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productoAll, 5)
        productoAll = paginator.page(page)
    except:
        raise Http404

    datos = {
        'tabla' : productoAll, 'paginator' : paginator

    }

    return render(request, 'app/admin/tabla.html', datos)

def registrar_user(request):
    datos = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, usuario)

            return redirect(to="index")
        datos['form']=formulario

    return render(request, 'registration/register.html',datos)

def subscripsion(request):
    usuario = Subscripcion(usuario=request.user)
    subAll = Subscripcion.objects.all()
    datos = {
        'formulario' : SubscripcionForm(instance=usuario),
        'tabla' : subAll
    }
    if request.method == 'POST':
        formulario = SubscripcionForm(data=request.POST, files= request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()

            odd_even = Permission.objects.get(name='Can view subscripcion')
            user_yui = User.objects.get(username=request.user)
            user_yui.user_permissions.add(odd_even)
            user_yui.save()
            odd_even = Permission.objects.get(name='Can delete subscripcion')
            user_yui.user_permissions.add(odd_even)
            user_yui.save()
            
            datos['mensaje'] = 'Subscripcion exitosa!'
            datos['formulario'] = formulario

            return redirect(to="subscripcion")

    return render(request, 'registration/subscripcion.html', datos)

def eliminar_sub(request, id):
    sub = Subscripcion.objects.get(id=id)
    sub.delete()

    return redirect(to='subscripcion')



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscriptionSerializer
    
