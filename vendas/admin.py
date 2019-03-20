from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Ecommerce


@admin.register(Ecommerce)
class CategoriaResource(ImportExportModelAdmin):
    pass
