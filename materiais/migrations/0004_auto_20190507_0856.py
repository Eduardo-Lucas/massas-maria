# Generated by Django 2.0.2 on 2019-05-07 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globais', '0001_initial'),
        ('materiais', '0003_auto_20190320_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globais.Uf')),
            ],
            options={
                'verbose_name': 'Cadastro de Loja',
                'verbose_name_plural': 'Cadastro de Lojas',
            },
        ),
        migrations.AddField(
            model_name='pedidoweb',
            name='loja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiais.Loja'),
        ),
    ]
