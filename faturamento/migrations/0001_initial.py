# Generated by Django 2.0.2 on 2020-05-07 15:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globais', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoParticipante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, unique=True, verbose_name='Código do Grupo de participantes')),
                ('descricao', models.CharField(max_length=80, verbose_name='Descrição do Grupo de participantes')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', help_text='Desabilite este Grupo caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Grupo de Participante',
                'verbose_name_plural': 'Grupos de Participantes',
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_nfe', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)], verbose_name='Número da Nota Fiscal')),
                ('serie_nfe', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Série da Nota Fiscal')),
                ('subserie_nfe', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999)], verbose_name='SubSérie da Nota fiscal')),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cadastro de notas fiscais emitidas e recebidas',
                'verbose_name_plural': 'Cadastro de notas fiscais emitidas e recebidas',
                'ordering': ['numero_nfe'],
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=50)),
                ('nome_fantasia', models.CharField(max_length=50, verbose_name='Nome Fantasia')),
                ('fisica_juridica', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], default='J', max_length=1, verbose_name='Pessoa Física(F) ou Jurídica (J)')),
                ('cnpj_cpf', models.CharField(blank=True, max_length=14, null=True, verbose_name='CNPJ/CPF')),
                ('inscricao_estadual', models.CharField(default='ISENTO', max_length=15, verbose_name='Inscricao Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, default='ISENTO', max_length=15, verbose_name='Inscrição Municipal')),
                ('codigo', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)], verbose_name='Código')),
                ('endereco', models.CharField(blank=True, max_length=60, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=60, null=True, verbose_name='Complemento')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=10, null=True, verbose_name='Bairro')),
                ('cep', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)], verbose_name='CEP')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 2')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular 1')),
                ('celular2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular 2')),
                ('email', models.CharField(blank=True, max_length=40, null=True, verbose_name='E-mail')),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globais.Municipio')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globais.Uf')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faturamento.GrupoParticipante')),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globais.PaisIbge')),
            ],
            options={
                'verbose_name': 'Cadastro de Participante',
                'verbose_name_plural': 'Cadastro de Participantes',
                'ordering': ['razao_social'],
            },
        ),
        migrations.CreateModel(
            name='RegiaoDeVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, unique=True, verbose_name='Código da região de vendas')),
                ('descricao', models.CharField(max_length=80, verbose_name='Descrição da região de vendas')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Desabilite este CFOP caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
                ('ultima_alteracao', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Região de Venda',
                'verbose_name_plural': 'Regiões de Vendas',
                'ordering': ('descricao',),
            },
        ),
        migrations.AddField(
            model_name='participante',
            name='regiao_de_venda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='faturamento.RegiaoDeVenda'),
        ),
        migrations.AddField(
            model_name='participante',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='responsavel', to=settings.AUTH_USER_MODEL),
        ),
    ]
