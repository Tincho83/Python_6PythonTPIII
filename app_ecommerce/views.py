from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Cliente, Producto, Pedido, Categoria, ContadorVisitas, TipoDoc
from .forms import ClienteForm, ProductoForm, PedidoForm, CategoriaForm, TipoDocForm

def index(request):
    # Contador de visitas únicas por sesión
    session_key = 'visitado'
    contador, _ = ContadorVisitas.objects.get_or_create(pk=1)

    if not request.session.get(session_key, False):
        contador.total += 1
        contador.save()
        request.session[session_key] = True

    # Mostramos los primeros 4 productos
    productos = Producto.objects.all()[:4]

    return render(request, 'app_ecommerce/index.html', {
        'productos': productos,
        'contador_visitas': contador.total
    })



def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'app_ecommerce/cliente_form.html', {'form': form})


def producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'app_ecommerce/producto_form.html', {'form': form})


def pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            #form.save()
            pedido = form.save()
            messages.success(request, f"Pedido #{pedido.id} registrado correctamente.")
            return redirect('pedido')
    else:
        form = PedidoForm()
    return render(request, 'app_ecommerce/pedido_form.html', {'form': form})


def categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'app_ecommerce/categoria_form.html', {'form': form})


def tipodoc(request):
    if request.method == "POST":
        form = TipoDocForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TipoDocForm()
    return render(request, 'app_ecommerce/tipodoc_form.html', {'form': form})



def buscar(request):
    #query = request.GET.get('q')
    query = request.GET.get('q', '')
    resultados = []
    #if query:
    if len(query) > 0:
        resultados = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    else:
        resultados = Producto.objects.all().order_by("-precio")
    
    return render(request, 'app_ecommerce/buscar.html', {'resultados': resultados, 'query': query})
