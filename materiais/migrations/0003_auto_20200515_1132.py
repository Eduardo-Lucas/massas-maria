# Generated by Django 2.0.2 on 2020-05-15 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_remove_pedidowebitem_participante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidoweb',
            options={'ordering': ['-id'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='pedidowebitem',
            options={'ordering': ['-pedidoweb', 'sequencia'], 'verbose_name': 'Pedido Item', 'verbose_name_plural': 'Pedidos Itens'},
        ),
    ]
