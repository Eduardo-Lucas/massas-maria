# Generated by Django 2.0.2 on 2020-05-19 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20200519_1109'),
        ('faturamento', '0011_auto_20200519_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='tabelapreco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empresas.TabelaPreco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participante',
            name='tipo_participante',
            field=models.CharField(choices=[('cliente', 'Cliente'), ('fornecedor', 'Fornecedor'), ('ambos', 'Ambos'), ('transportadora', 'Transportadora')], default='cliente', max_length=20),
        ),
    ]