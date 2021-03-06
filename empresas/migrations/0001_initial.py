# Generated by Django 2.0.2 on 2020-05-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True)),
                ('logotipo', models.ImageField(blank=True, upload_to='empresas')),
                ('tipo', models.CharField(choices=[('Física', 'Fisica'), ('Jurídica', 'Juridica')], default='Jurídica', max_length=10)),
                ('ativo', models.BooleanField(default=True, verbose_name='Status do cliente')),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('rg', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('indicador_inscricao_estadual', models.CharField(choices=[('Não contribuinte', 'Não contribuinte'), ('Contribuinte', 'Contribuinte'), ('Contribuinte isento', 'Contribuinte isento')], default='Não contribuinte', max_length=20)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, null=True)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=20, null=True)),
                ('inscricao_SUFRAMA', models.CharField(blank=True, max_length=20, null=True)),
                ('optante_simples', models.BooleanField(default=False, max_length=1)),
                ('email', models.EmailField(help_text='Informe apenas um e-mail', max_length=254)),
                ('telefone_comercial', models.CharField(default='(071) 9 9999-9999', max_length=20)),
                ('telefone_celular', models.CharField(default='(071) 9 9999-9999', max_length=20)),
                ('data_fundacao', models.DateField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('observacao', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observações')),
                ('nome_contato', models.CharField(blank=True, max_length=50, null=True)),
                ('email_contato', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone_contato', models.CharField(blank=True, max_length=20, null=True)),
                ('cargo_contato', models.CharField(blank=True, max_length=20, null=True)),
                ('cep', models.CharField(default=41000, max_length=8)),
                ('endereco', models.CharField(default='Rua do Sobe e Desce', max_length=50)),
                ('numero', models.CharField(default='s/n', max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=10, null=True)),
                ('bairro', models.CharField(blank=True, max_length=20, null=True)),
                ('cidade', models.CharField(default='Salvador', max_length=20)),
                ('uf', models.CharField(default='SC', max_length=2)),
                ('pais', models.CharField(default='Brasil', max_length=15)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='empresa',
            unique_together={('nome', 'codigo')},
        ),
    ]
