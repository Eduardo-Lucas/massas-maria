from import_export import resources

from empresas.models import Empresa, TabelaPreco, TabelaPrecoItem


class EmpresaResource(resources.ModelResource):
    class Meta:
        model = Empresa
        fields = '__all__'


class TabelaPrecoResource(resources.ModelResource):
    class Meta:
        model = TabelaPreco
        fields = '__all__'


class TabelaPrecoItemResource(resources.ModelResource):
    class Meta:
        model = TabelaPrecoItem
        fields = '__all__'
