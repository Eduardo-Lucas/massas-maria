from materiais.models import PedidoWeb, Produto

import django_filters


class PedidoWebFilter(django_filters.FilterSet):
    
    class Meta:
        model = PedidoWeb
        fields = ['status_pedido', 'participante', 'tipo_de_pagamento', 'prazo_de_pagamento', 'vendedor', ]
        

class ProdutoFilter(django_filters.FilterSet):
    min_preco_venda = django_filters.NumberFilter(field_name="preco_venda", lookup_expr='gte')
    max_preco_venda = django_filters.NumberFilter(field_name="preco_venda", lookup_expr='lte')

    class Meta:
        model = Produto
        fields = ['categoria', 'disponivel', 'min_preco_venda', 'max_preco_venda', ]
