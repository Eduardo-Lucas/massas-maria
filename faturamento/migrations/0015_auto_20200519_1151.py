# Generated by Django 2.0.2 on 2020-05-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faturamento', '0014_auto_20200519_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro'),
        ),
    ]
