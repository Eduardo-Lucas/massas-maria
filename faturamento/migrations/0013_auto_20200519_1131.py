# Generated by Django 2.0.2 on 2020-05-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faturamento', '0012_auto_20200519_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='celular2',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='telefone2',
        ),
        migrations.AlterField(
            model_name='participante',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone'),
        ),
    ]
