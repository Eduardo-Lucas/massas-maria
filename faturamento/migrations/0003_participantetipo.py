# Generated by Django 2.0.2 on 2020-05-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faturamento', '0002_participante_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipanteTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Participante',
                'verbose_name_plural': 'Tipos de Participantes',
                'ordering': ('nome',),
            },
        ),
    ]