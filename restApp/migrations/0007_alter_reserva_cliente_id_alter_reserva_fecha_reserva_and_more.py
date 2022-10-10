# Generated by Django 4.1.2 on 2022-10-10 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0006_alter_reserva_cliente_id_alter_reserva_mesa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.CharField(blank=True, default='DD-MM-AAAA', max_length=12),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(blank=True, default='HH:MM', max_length=5),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='mesa',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.mesa'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='numero_plato',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='pedido',
            field=models.CharField(blank=True, choices=[('D', 'Delivery'), ('R', 'Restaurante')], default='R', max_length=2),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='plato',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.plato'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='sucursal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restApp.sucursal'),
        ),
    ]