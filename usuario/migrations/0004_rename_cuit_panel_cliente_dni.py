# Generated by Django 4.1.2 on 2022-11-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_panel_cliente_direccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panel_cliente',
            old_name='cuit',
            new_name='dni',
        ),
    ]
