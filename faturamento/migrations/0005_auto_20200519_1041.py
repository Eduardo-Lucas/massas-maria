# Generated by Django 2.0.2 on 2020-05-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faturamento', '0004_delete_participantetipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]