# Generated by Django 4.2.1 on 2023-06-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.TextField()),
                ('descripcion_producto', models.TextField()),
                ('precio_producto', models.TextField()),
                ('stock_producto', models.TextField()),
                ('imagen_producto', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
    ]
