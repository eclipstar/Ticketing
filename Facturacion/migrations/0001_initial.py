# Generated by Django 2.1.7 on 2019-06-16 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Total')),
                ('cantidadProductos', models.IntegerField(verbose_name='Cantidad de Productos')),
                ('tipoPago', models.CharField(max_length=50, verbose_name='Tipo de Pago')),
                ('tiempoRestante', models.TimeField(verbose_name='Tiempo Restante')),
                ('entregado', models.BooleanField(verbose_name='')),
                ('cancelado', models.BooleanField(verbose_name='')),
                ('codigoCompra', models.CharField(max_length=50, verbose_name='Codigo Compra')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='LineaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre')),
                ('cantidad', models.IntegerField(verbose_name=())),
                ('tipoProducto', models.CharField(blank=True, max_length=100, null=True)),
                ('idProducto', models.IntegerField(verbose_name='idProducto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='subtotal')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='Facturacion.Carrito')),
            ],
            options={
                'verbose_name': 'LineaVenta',
                'verbose_name_plural': 'LineaVentas',
            },
        ),
        migrations.CreateModel(
            name='TarjetaCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='')),
                ('fechaVencimiento', models.DateField(verbose_name='')),
                ('ccv', models.IntegerField(verbose_name='')),
                ('marca', models.CharField(max_length=50, verbose_name='')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titular', to='Facturacion.Cliente')),
            ],
            options={
                'verbose_name': 'Tajeta de Credito',
                'verbose_name_plural': 'TajetaCreditos',
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturacion.TarjetaCredito'),
        ),
    ]
