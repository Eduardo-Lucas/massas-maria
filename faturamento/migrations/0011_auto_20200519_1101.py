# Generated by Django 2.0.2 on 2020-05-19 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faturamento', '0010_auto_20200519_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='regiao_de_venda',
        ),
    ]
