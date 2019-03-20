# Generated by Django 2.0.2 on 2019-03-16 21:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cfop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Código CFOP')),
                ('descricao', models.CharField(max_length=512, verbose_name='Descrição do CFOP')),
                ('natureza_base_calc_cred_pis', models.CharField(max_length=2, verbose_name='Base de Cálculo do Crédito: SPED PIS COFINS')),
                ('dias_devolucao', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Número de dias para Devolução')),
                ('pode_subst_tributaria', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='CFOP pode ter Substituição Tributária?')),
                ('tributado_icms', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Calcular tributação de Icms?')),
                ('credito_icms', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Pode ter crédidos de icms?')),
                ('reduz_base_icms', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Pode ter redução de Base?')),
                ('operacao_icms', models.CharField(choices=[('1', 'Operação   com crédito de impostos - IPI'), ('2', 'Operação   sem crédito imp - ISENTAS/NAO TRIBUTADAS - IPI'), ('3', 'Operação   sem crédito imposto - OUTRAS IPI ')], default='1', max_length=1, verbose_name='Operação com ICMS nos Livros Fiscais')),
                ('tributado_ipi', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Cfop tem tributação de IPI?')),
                ('credito_ipi', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Permite Crédito de IPI?')),
                ('operacao_ipi', models.CharField(choices=[('1', 'Operação   com crédito de impostos'), ('2', 'Operação   sem crédito imp - ISENTAS/NAO TRIBUTADAS'), ('3', 'Operação   sem crédito imposto - OUTRAS')], default='1', max_length=1, verbose_name='Operação com IPI nos Livros Fiscais')),
                ('tributado_pis_cofins', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Calcular tributação de Pis/Cofins?')),
                ('credito_pis_cofins', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Permite Crédito de Pis/Cofins?')),
                ('cfop_padrao', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Cfop é padrão em todos os itens?')),
                ('movimenta_estoques', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Cfop é padrão em todos os itens?')),
                ('movimenta_financeiro', models.CharField(choices=[('S', 'Financeiro obrigatório  NF=PAGAR'), ('N', 'Financeiro NÃO é obrigatório  na NF'), ('B', 'NFe NÃO tem financeiro (Bonificação, etc)'), ('A', 'Apenas Avisa ao usuário para decidir')], default='S', max_length=1, verbose_name='Financeiro na Nfe será obrigatório?')),
                ('calcula_custos', models.CharField(choices=[('S', 'S_Calcula Custo e Custo médio nas entradas'), ('N', 'N_Não calcula Custos nas entradas')], default='S', max_length=1, verbose_name='Calcular preços de Custos')),
                ('custo_icms', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='-', max_length=1, verbose_name='Icms no Custo')),
                ('custo_ipi', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Ipi no Custo')),
                ('custo_frete', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Frete no Custo')),
                ('custo_icms_frete', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='-', max_length=1, verbose_name='Icms do Frete no Custo')),
                ('custo_pis', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='-', max_length=1, verbose_name='Pis no Custo')),
                ('custo_cofins', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='-', max_length=1, verbose_name='Cofins no Custo')),
                ('custo_seguro', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Seguro no Custo')),
                ('custo_despesas', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Despesas no Custo')),
                ('custo_descontos', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='-', max_length=1, verbose_name='Descontos no Custo')),
                ('custo_icms_sub', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Icms Subs no Custo')),
                ('custo_antecipacao_trib', models.CharField(choices=[('-', 'Tem Crédito - Subtrai valor do custo na nf (icm)'), ('+', 'Soma valor ao preco da NF (Ex. IPI/FRETE)'), ('I', 'Ignora valor, não  soma nem subtrai no custo')], default='+', max_length=1, verbose_name='Icms Subs no Custo')),
                ('finalidade_nfe', models.CharField(choices=[('1', '1_NF-e normal'), ('2', '2_NF-e complementar'), ('3', '3_NF-e de ajuste'), ('4', '4_NF-e Devolução/retorno')], default='+', max_length=1, verbose_name='Finalidade padrão na Emissão da NFe')),
                ('doc_referenciado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='+', max_length=1, verbose_name='Calcular preços de Custos')),
            ],
            options={
                'verbose_name': 'CFOP',
                'verbose_name_plural': 'CFOPs',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='CodigoCest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7, verbose_name='Código')),
                ('descricao', models.CharField(max_length=350, verbose_name='Descrição')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
            ],
            options={
                'verbose_name': 'Código CEST',
                'verbose_name_plural': 'Códigos CEST',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='CodigoCnae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descricao', models.CharField(max_length=80)),
                ('tipo_atividade', models.CharField(max_length=80)),
                ('simples_nacional', models.BooleanField(default=False)),
                ('per_imposto', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('inscricao_estadual', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='CodigoNbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=7)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Código NBS',
                'verbose_name_plural': 'Códigos NBS',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='CodigoNcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('unidade', models.CharField(max_length=10)),
                ('data_publicacao', models.DateField()),
                ('data_validade', models.DateField(blank=True, null=True)),
                ('descricao_unidade', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Código NCM',
                'verbose_name_plural': 'Códigos NCM',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='ContaReferencialBacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_conta', models.CharField(max_length=20, unique=True)),
                ('descricao', models.CharField(max_length=80)),
                ('data_inicio', models.DateField(max_length=8)),
                ('data_fim', models.DateField(max_length=8)),
                ('tipo_conta', models.CharField(max_length=1)),
                ('conta_superior', models.CharField(max_length=20, unique=True)),
                ('nivel_contabil', models.PositiveSmallIntegerField()),
                ('codigo_natureza', models.CharField(max_length=1, unique=True)),
                ('utilizacao', models.CharField(max_length=1, unique=True)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='ContaReferencialDinamica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_conta', models.CharField(max_length=20, unique=True)),
                ('descricao', models.CharField(max_length=80)),
                ('data_inicio', models.DateField(max_length=8)),
                ('data_fim', models.DateField(max_length=8)),
                ('tipo_conta', models.CharField(max_length=1)),
                ('conta_superior', models.CharField(max_length=20, unique=True)),
                ('nivel_contabil', models.PositiveSmallIntegerField()),
                ('codigo_natureza', models.CharField(max_length=1, unique=True)),
                ('utilizacao', models.CharField(max_length=1, unique=True)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='ContaReferencialSusep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_conta', models.CharField(max_length=20, unique=True)),
                ('descricao', models.CharField(max_length=80)),
                ('data_inicio', models.DateField(max_length=8)),
                ('data_fim', models.DateField(max_length=8)),
                ('tipo_conta', models.CharField(max_length=1)),
                ('conta_superior', models.CharField(max_length=20, unique=True)),
                ('nivel_contabil', models.PositiveSmallIntegerField()),
                ('codigo_natureza', models.CharField(max_length=1, unique=True)),
                ('utilizacao', models.CharField(max_length=1, unique=True)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='MensagemPadrao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, unique=True, verbose_name='Codigo da Mensagem Padrao')),
                ('descricao', models.CharField(max_length=2048, verbose_name='Descrição do Mensagem?')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Desabilite esta mensagem caso sua empresa não a utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitada para uso')),
            ],
            options={
                'verbose_name': 'Mensagem Padrão',
                'verbose_name_plural': 'Mensagens Padrões',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloDocumentoFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, unique=True)),
                ('descricao', models.CharField(max_length=100)),
                ('data_validade', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Modelo de Documento Fiscal',
                'verbose_name_plural': 'Modelos de Documentos Fiscais',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999)])),
                ('descricao', models.CharField(max_length=80)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='PaisIbge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('descricao', models.CharField(max_length=60)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoDocumentoSped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('descricao', models.CharField(max_length=100)),
                ('data_validade', models.DateField(blank=True, max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'Situação Documento Sped',
                'verbose_name_plural': 'Situação Documentos Sped',
                'ordering': ('codigo',),
            },
        ),
        migrations.CreateModel(
            name='SituacaoTribCofins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('descricao', models.CharField(max_length=150)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
                ('data_validade', models.DateField(blank=True, null=True)),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Desabilite este cst caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
            ],
            options={
                'verbose_name': 'Situação Tributária COFINS',
                'verbose_name_plural': 'Situações Tributárias COFINS',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoTribIcms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)], verbose_name='Código')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data de Publicação')),
                ('data_validade', models.DateField(blank=True, null=True, verbose_name='Data de Validade')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', help_text='Desabilite esta Situação Tributária caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
            ],
            options={
                'verbose_name': 'Situação Tributária ICMS',
                'verbose_name_plural': 'Situações Tributárias ICMS',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoTribIpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Código')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data de Publicação')),
                ('data_validade', models.DateField(blank=True, null=True, verbose_name='Data de Validade')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', help_text='Desabilite Situação Tributária caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
            ],
            options={
                'verbose_name': 'Situação Tributária IPI',
                'verbose_name_plural': 'Situações Tributárias IPI',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoTribPis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)], verbose_name='Código')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data de Publicação')),
                ('data_validade', models.DateField(blank=True, null=True, verbose_name='Data de Validade')),
                ('habilitado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Desabilite este Situação Tributária caso sua empresa não o utilize ou utilize muito esporadicamente para evitar erros', max_length=1, verbose_name='Habilitado para uso')),
            ],
            options={
                'verbose_name': 'Situação Tributária PIS',
                'verbose_name_plural': 'Situações Tributárias PIS',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='TipoOperacaoFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, unique=True, verbose_name='Tipo de Operação Fiscal?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição do Operação ou Movimento Fiscal na empresa?')),
            ],
            options={
                'verbose_name': 'Tipo de Operação Fiscal',
                'verbose_name_plural': 'Tipos de Operações Fiscais',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('sigla_estado', models.CharField(max_length=2)),
                ('estado', models.CharField(max_length=50)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Unidade Federativa',
                'verbose_name_plural': 'Unidades Federativas',
                'ordering': ['sigla_estado'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='tipooperacaofiscal',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AlterUniqueTogether(
            name='situacaotribpis',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AlterUniqueTogether(
            name='situacaotribipi',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AlterUniqueTogether(
            name='situacaotribicms',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AlterUniqueTogether(
            name='situacaotribcofins',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AlterUniqueTogether(
            name='mensagempadrao',
            unique_together={('codigo', 'descricao')},
        ),
        migrations.AddField(
            model_name='cfop',
            name='mensagempadrao',
            field=models.ForeignKey(help_text='Mensagem padrão a ser impressa durante a emissão da nota fiscal como observações adicionais na NF', on_delete=django.db.models.deletion.CASCADE, to='globais.MensagemPadrao'),
        ),
        migrations.AddField(
            model_name='cfop',
            name='tipomovimentofiscal',
            field=models.ForeignKey(help_text='Tipo de movimento fiscal - Vendas/Compras/bonificação/etc - usado no BI e outros relatorios de vendas', on_delete=django.db.models.deletion.CASCADE, to='globais.TipoOperacaoFiscal'),
        ),
    ]
