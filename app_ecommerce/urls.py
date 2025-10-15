from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.cliente, name='cliente'),
    path('tipodoc/', views.tipodoc, name='tipodoc'),
    path('producto/', views.producto, name='producto'),
    path('pedido/', views.pedido, name='pedido'),
    path('categoria/', views.categoria, name='categoria'),
    path('buscar/', views.buscar, name='buscar'),
]
