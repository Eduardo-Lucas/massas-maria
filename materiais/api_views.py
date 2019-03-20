from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from materiais.filters import PedidoWebFilter
from materiais.models import PedidoWeb, PedidoWebItem, Produto, Categoria
from materiais.serializers import PedidoWebSerializer, PedidoWebItemSerializer, ProdutoSerializer, CategoriaSerializer

from rest_framework import viewsets

"""
    API views 
"""


class PedidoWebItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PedidoWebItem to be viewed or edited.
    API endpoint que  permite que PedidoWebItem seja visualizado ou editado.
    """
    queryset = PedidoWebItem.objects.all().order_by('sequencia')
    serializer_class = PedidoWebItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['pedidoweb', 'produto', ]


class PedidoWebViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PedidoWeb to be viewed or edited.
    API endpoint que  permite que PedidoWeb seja visualizado ou editado.
    """
    queryset = PedidoWeb.objects.all().order_by('-id')
    serializer_class = PedidoWebSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = PedidoWebFilter
    filter_fields = ['status_pedido']
    

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Produto be viewed or edited.
    API endpoint que  permite que Produto seja visualizado ou editado.
    """
    queryset = Produto.objects.all().order_by('descricao')
    serializer_class = ProdutoSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['categoria', 'disponivel']


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categoria be viewed or edited.
    API endpoint que  permite que Categoria seja visualizado ou editado.
    """
    queryset = Categoria.objects.all().order_by('nome')
    serializer_class = CategoriaSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('nome', )


