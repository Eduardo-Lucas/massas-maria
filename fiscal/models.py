from django.db import models
from django_filters.rest_framework import FilterSet, DateFromToRangeFilter


class Article(models.Model):
    published = models.DateTimeField()


class F(FilterSet):
    published = DateFromToRangeFilter()

    class Meta:
        model = Article
        fields = ['published']
