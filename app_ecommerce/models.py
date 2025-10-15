from django.db import models

# Create your models here.

class TipoDoc(models.Model):
    nombre = models.CharField(max_length=7, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=51)
    apellido = models.CharField(max_length=51)
    tipodoc = models.ForeignKey(TipoDoc, on_delete=models.CASCADE, related_name="clientes")
    nrodoc = models.IntegerField(unique=True)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}. {self.tipodoc}: {self.nrodoc}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=254, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.producto.precio * self.cantidad
        
    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"

class ContadorVisitas(models.Model):
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitas totales: {self.total}"




