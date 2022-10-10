from datetime import datetime
from pickletools import long1
from sqlite3 import Date
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Mesa, Plato, PedidoChoice, Sucursal, Reserva
from .forms import ReservaForm

def index(request):
    return HttpResponse("hola mundo")

def client(request, sucursal):
    return HttpResponse(f"Bienvenido a {sucursal}")

""" def clientes(request):
    return render(request, "cliente.html") """

def reserva_view(request):
    form = ReservaForm()
    reserva = None
    id_reserva = request.GET.get('id')
    if id_reserva:
        reserva = Reserva.objects.get(id=id_reserva)
        form=ReservaForm(instance=reserva)

    if request.method == 'POST':
        if reserva:
            form = ReservaForm(request.POST, instance=reserva)
        else:
            form= ReservaForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "reservaC.html",{"form":form})



def clientes_form(request):
    nombreCliente = request.POST.get('nombreCliente')
    paternoCliente = request.POST.get('paternoCliente')
    maternoCliente = request.POST.get('maternoCliente')
    ciCliente = request.POST.get('ciCliente')
    fonoCliente = request.POST.get('fonoCliente')
    emailCliente = request.POST.get('emailCliente')
    if ciCliente:
        q = Cliente(nombre = nombreCliente, paterno=paternoCliente, materno=maternoCliente,  ci=ciCliente, telefono=fonoCliente, correo=emailCliente)
        q.save()
    return render(request, "cliente.html")