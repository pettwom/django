from django.contrib import admin

from .models import Sucursal
from .models import Mesa
from .models import Cliente
from .models import Reserva
from .models import Plato
from .models import Pedido

admin.site.site_header="RESTAURANTE PETTER"
admin.site.index_title= "PANEL DE CONTROL"

class SucursalAdmin(admin.ModelAdmin):
    list_display=('nombre_admin','nombre_sucursal', 'direccion_sucursal','telefono_sucursal')
    ordering=['direccion_sucursal']
    list_filter=('nombre_sucursal', 'direccion_sucursal') 
    search_fields=("nombre_sucursal", 'nombre_admin')

class MesaAdmin(admin.ModelAdmin):
    list_display=('numero_mesa','cantidad_sillas','status_mesa','sucursal')
    ordering=['status_mesa']

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','paterno', 'materno','ci','telefono','correo')
    ordering=['ci']
    list_filter=('paterno', 'materno') 
    search_fields=("paterno", 'materno','telefono','correo')    

class ReservaAdmin(admin.ModelAdmin):
    list_display=('id','sucursal','cliente','fecha_reserva','hora_reserva','cliente_id','mesa')
    ordering=['fecha_reserva','hora_reserva']
    list_display_links=('fecha_reserva','hora_reserva')

class PlatoAdmin(admin.ModelAdmin):
    list_display=("nombrePlato",'precio','descripcion','status')
    ordering=['status']
    list_editable=('status','precio')

class PedidoAdmin(admin.ModelAdmin):
    list_display=('cliente','platos','cantidad_pedido','pedido', 'categoriaComida', 'categoriaRefresco','cantidad_refresco')
    ordering=['cliente']
    list_filter=('cliente','platos','pedido')
    list_editable=('platos','pedido')


admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Pedido, PedidoAdmin)