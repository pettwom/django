from django.urls import path
from . import views

urlpatterns=[
    path('reserva/',views.reserva_view, name="reserva_view"),
    path('clientes/',views.clientes_form, name="cliente_form"),
    path('cliente/<str:sucursal>',views.client, name="cliente"),
    path('', views.index, name='index')
    
]