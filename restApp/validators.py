
from django.core.exceptions import ValidationError

def validar_precio(value):
        if(value>=280 and value<0):
            raise ValidationError(
                'El monto de %(value) Bs. no es válido', params={'value':value}
            )


def validar_platos(value):
        if(value>=10 and value<0):
            raise ValidationError(
                'La cantidad de %(value) platos. no es válida', params={'value':value}
            )            