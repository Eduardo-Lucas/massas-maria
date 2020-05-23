from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from empresas.models import Empresa, TabelaPreco, TabelaPrecoItem


@admin.register(Empresa)
class EmpresaResource(ImportExportModelAdmin):
    pass


@admin.register(TabelaPreco)
class TabelaPrecoResource(ImportExportModelAdmin):
    pass


@admin.register(TabelaPrecoItem)
class TabelaPrecoItemResource(ImportExportModelAdmin):
    pass
