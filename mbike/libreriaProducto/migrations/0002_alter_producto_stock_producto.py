# Generated by Django 4.2.1 on 2023-06-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreriaProducto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock_producto',
            field=models.IntegerField(),
        ),
    ]
