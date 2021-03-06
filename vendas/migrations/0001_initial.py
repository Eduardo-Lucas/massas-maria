# Generated by Django 2.0.2 on 2020-05-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('B2B', 'Business to Business - discount'), ('B2C', 'Business to Customer - no discount')], default='B2C', max_length=3)),
            ],
            options={
                'verbose_name': 'E-Commerce',
                'verbose_name_plural': 'E-Commerces',
                'ordering': ['tipo'],
            },
        ),
    ]
