from django.db import models

from choices.models import ECOMMERCE_TIPO_CHOICES


class Ecommerce(models.Model):
    tipo = models.CharField(max_length=3, choices=ECOMMERCE_TIPO_CHOICES, default='B2C')

    def __str__(self):
        if self.tipo == 'B2B':
           return self.tipo + ' - COM desconto'
        else:
           return self.tipo + ' - SEM desconto'


    class Meta:
        ordering = ['tipo'] 
        verbose_name = 'E-Commerce'
        verbose_name_plural = 'E-Commerces'
