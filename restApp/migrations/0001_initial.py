# Generated by Django 4.1.2 on 2022-10-09 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('paterno', models.CharField(max_length=200)),
                ('materno', models.CharField(max_length=200)),
                ('ci', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mesa', models.CharField(default='Mesa Nro. ', max_length=11)),
                ('cantidad_sillas', models.IntegerField()),
                ('status_mesa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePlato', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sucursal', models.CharField(max_length=200, unique=True)),
                ('direccion_sucursal', models.TextField()),
                ('telefono_sucursal', models.CharField(max_length=8)),
                ('nombre_admin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.CharField(max_length=12)),
                ('hora_reserva', models.CharField(max_length=5)),
                ('numero_plato', models.IntegerField()),
                ('pedido', models.CharField(choices=[('D', 'Delivery'), ('R', 'Restaurante')], default='R', max_length=2)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.cliente')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.mesa')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.plato')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_pedido', models.IntegerField()),
                ('categoriaComida', models.CharField(choices=[('al', 'almuerzos'), ('cr', 'Carne Roja'), ('cb', 'Carne blanca'), ('p', 'Pastas'), ('pt', 'Platos Típicos'), ('par', 'Parrilla')], default='al', max_length=3)),
                ('categoriaRefresco', models.CharField(choices=[('rh', 'Refrescos Hervidos'), ('g', 'Gaseosas'), ('a', 'Agua'), ('lca', 'Líquidos con Alcohol')], default='a', max_length=3)),
                ('pedido', models.CharField(choices=[('D', 'Delivery'), ('R', 'Restaurante')], default='R', max_length=2)),
                ('cantidad_refresco', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.cliente')),
                ('platos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.plato')),
            ],
        ),
        migrations.AddField(
            model_name='mesa',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.sucursal'),
        ),
    ]
