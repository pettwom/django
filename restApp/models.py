from enum import unique
from random import choices
from wsgiref.validate import validator
from .validators import validar_precio
from .validators import validar_platos
from django.db import models

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length = 200, unique= True)
    direccion_sucursal= models.TextField()
    telefono_sucursal= models.CharField(max_length = 8)
    nombre_admin = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre_sucursal

class Mesa(models.Model):
    numero_mesa = models.CharField(max_length= 11, default="Mesa Nro. ")
    cantidad_sillas = models.IntegerField()
    status_mesa = models.BooleanField(default = True)
    sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE)

    def __str__(self):
        return self.numero_mesa

class Cliente(models.Model):
    nombre= models.CharField(max_length = 200)
    paterno = models.CharField(max_length = 200)
    materno = models.CharField(max_length = 200)
    ci = models.IntegerField()
    correo = models.EmailField(max_length = 254 )
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre +' '+self.paterno + ' '+self.materno

class CategoriaComida(models.TextChoices):
    AL = 'al','almuerzos'
    CR = 'cr', 'Carne Roja'
    CB = 'cb', 'Carne blanca'
    P = 'p' , 'Pastas'
    PT = 'pt', 'Platos Típicos'
    PAR = 'par', 'Parrilla'

class CategoriaRefrescos(models.TextChoices):
    RH = 'rh', 'Refrescos Hervidos'
    G = 'g', 'Gaseosas'
    A='a', 'Agua'
    LCA = 'lca','Líquidos con Alcohol'

class Plato(models.Model):
    nombrePlato = models.CharField(max_length = 200)
    precio = models.IntegerField(validators=[validar_precio])
    status = models.BooleanField(default = True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombrePlato

class PedidoChoice(models.TextChoices):
    D = 'D','Delivery'
    R = 'R', 'Restaurante'

class Reserva(models.Model):
    fecha_reserva =models.CharField(max_length=12, default='DD-MM-AAAA',  null=True) 
    hora_reserva = models.CharField(max_length=5, default='HH:MM', null=True)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE, null=True)
    mesa = models.ForeignKey(Mesa, on_delete = models.CASCADE,  null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete = models.CASCADE,  null=True)
    plato = models.ForeignKey(Plato, on_delete = models.CASCADE, null=True)
    numero_plato = models.IntegerField( null=True, validators=[validar_platos])
    pedido = models.CharField(max_length= 2, choices = PedidoChoice.choices, default = PedidoChoice.R, null=True)



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    platos = models.ForeignKey(Plato, on_delete= models.CASCADE)
    cantidad_pedido = models.IntegerField()
    categoriaComida = models.CharField(max_length = 3, choices = CategoriaComida.choices, default = CategoriaComida.AL)
    categoriaRefresco = models.CharField(max_length = 3, choices= CategoriaRefrescos.choices, default = CategoriaRefrescos.A)
    pedido = models.CharField(max_length= 2, choices = PedidoChoice.choices, default = PedidoChoice.R)
    cantidad_refresco = models.IntegerField()

    