# Generated by Django 4.1.2 on 2022-10-10 02:30

from django.db import migrations, models
import django.db.models.deletion
import restApp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0010_alter_reserva_cliente_alter_reserva_fecha_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.CharField(default='DD-MM-AAAA', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(default='HH:MM', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='mesa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.mesa'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='numero_plato',
            field=models.IntegerField(null=True, validators=[restApp.validators.validar_platos]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pedido',
            field=models.CharField(choices=[('D', 'Delivery'), ('R', 'Restaurante')], default='R', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='plato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.plato'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.sucursal'),
        ),
    ]
