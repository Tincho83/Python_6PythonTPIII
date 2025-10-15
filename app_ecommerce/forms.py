from django import forms
from .models import Cliente, Producto, Pedido, Categoria, TipoDoc

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "tipodoc", "nrodoc", "email", "fecha_nacimiento", "domicilio"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "apellido" : forms.TextInput(attrs={'class': 'form-control'}),
            #"tipodoc" : forms.TextInput(attrs={'class': 'form-control'}),
            "tipodoc" :forms.Select(attrs={'class': 'form-control'}),
            "nrodoc" : forms.NumberInput(attrs={'class': 'form-control'}),
            "email" : forms.EmailInput(attrs={'class': 'form-control'}),
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control' }),
            "domicilio" : forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipodoc'].empty_label = "Seleccione un tipo de documento"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "imagen", "precio", "stock", "categoria"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
            "imagen" : forms.TextInput(attrs={'class': 'form-control'}),
            "precio" : forms.TextInput(attrs={'class': 'form-control'}),
            "stock" : forms.TextInput(attrs={'class': 'form-control'}),
            "categoria" : forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Seleccione una categoria"



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = "Seleccione un cliente"
        self.fields['producto'].empty_label = "Seleccione un producto"



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre","descripcion"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoDocForm(forms.ModelForm):
    class Meta:
        model = TipoDoc
        fields = ["nombre","descripcion"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

