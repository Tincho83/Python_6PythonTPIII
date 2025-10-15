from django.contrib import admin
from app_ecommerce.models import *

#admin.site.register(Cliente)
#admin.site.register(TipoDoc)
#admin.site.register(Categoria)
#admin.site.register(Producto)
#admin.site.register(Pedido)
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "tipodoc", "nrodoc", "email", "fecha_registro", "fecha_nacimiento", "domicilio")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nrodoc",)
    list_filter = ("fecha_registro", "fecha_nacimiento")
    ordering = ("apellido", "nombre", "nrodoc")
    readonly_fields = ("fecha_registro",)


@admin.register(TipoDoc)
class TipoDocAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre", "descripcion")
    ordering = ("nombre", "descripcion")
    readonly_fields = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre", "descripcion")
    ordering = ("nombre", "descripcion")
    readonly_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "imagen", "precio", "stock", "categoria")
    list_display_links = ("nombre", "categoria", "stock")
    search_fields = ("nombre",)
    list_filter = ("nombre", "categoria")
    ordering = ("nombre", "categoria", "descripcion")
    readonly_fields = ("categoria",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "producto", "cantidad", "fecha_pedido")
    list_display_links = ("cliente", "producto", "fecha_pedido")
    search_fields = ("cliente",)
    list_filter = ("cliente", "fecha_pedido")
    ordering = ("cliente", "producto", "fecha_pedido")
    readonly_fields = ("fecha_pedido",)