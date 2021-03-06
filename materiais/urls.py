from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PedidoWebTradicionalList, PedidoWebTradicionalDetalhe, \
    PedidoWebTradicionalUpdate, ProdutoDetalhe, ProdutoCreate, ProdutoList, manage_pedidowebitem, PedidoWebDelete, \
    PedidoWebItemDelete, PedidoWebItemUpdate, pedidowebitemcreate, search_pedidoweb, order_create, order_update, \
    produto_detail, expedicao, inicia_separacao, finaliza_separacao, estorna_separacao, AlteraLojaUpdate, \
    exporta_pedido_csv, exporta_pedido_excel, exporta_pedidoitem_excel

app_name = 'materiais'

urlpatterns = [
    
    # Pedido Tipo: Tradicional
    url(r'^pedidoweb_list/$', PedidoWebTradicionalList.as_view(), name='pedidoweb_list'),
    url(r'^pedidoweb_detail/(?P<pk>[0-9]+)/$', PedidoWebTradicionalDetalhe.as_view(), name="pedidoweb_detail"),
    url(r'^pedidoweb_edit/(?P<pk>[0-9]+)/edit/$', PedidoWebTradicionalUpdate.as_view(), name='pedidoweb_edit'),  
    
    url(r'^pedidoweb_delete/(?P<pk>[0-9]+)/delete/$', PedidoWebDelete.as_view(), name='pedidoweb_delete'),  
    
    url(r'^pedidowebitem_delete/(?P<pk>[0-9]+)/delete/$', PedidoWebItemDelete.as_view(), name='pedidowebitem_delete'),  

    url(r'^manage_pedidowebitem/(?P<pk>[0-9]+)/$', manage_pedidowebitem, name='manage_pedidowebitem'),

    # Edita Item do Pedido
    path('edita_item_pedido/(<pk>[0-9]+)/', PedidoWebItemUpdate.as_view(), name='edita_item_pedido'),
    
    # Adiciona Item no Pedido
    path('adiciona_item_pedido/(<pk>[0-9]+)/', pedidowebitemcreate, name='adiciona_item_pedido'),
    
    url(r'^create/$', order_create, name='order_create'),
    
    path('update/', order_update, name='order_update'),
    
    # Pedido Tipo: E-Commerce
    # url(r'', views.ProdutoList.as_view(), name='produto_list'),
    url(r'^produto_list/$', ProdutoList.as_view(), name='produto_list'),
    url(r'^produto_list/(?P<categoria_slug>[-\w]+)/$', ProdutoList.as_view(), name='produto_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.produto_detail, name='produto_detail'),
    url(r'^produto_list/(?P<id>\d+)/(?P<slug>[-\w]+)/$', produto_detail, name='produto_detail'),
    url(r'^produto_detalhe/(?P<pk>[0-9]+)/$', ProdutoDetalhe.as_view(), name="produto_detalhe"),
    url(r'^produto_add/$', ProdutoCreate.as_view(), name='produto_add'),

    # Index
    path('', ProdutoList.as_view(), name='home'),

    # Search PedidoWeb
    path('search_pedidoweb/', search_pedidoweb, name='search_pedidoweb'),
    
    path('expedicao/', expedicao, name='expedicao'),
    path('inicia_separacao/(<id>[0-9]+)/', inicia_separacao, name='inicia_separacao'),
    path('finaliza_separacao/(<id>[0-9]+)/', finaliza_separacao, name='finaliza_separacao'),
    path('estorna_separacao/(<id>[0-9]+)/', estorna_separacao, name='estorna_separacao'),
    path('altera_loja/(<pk>[0-9]+)/', AlteraLojaUpdate.as_view(), name='altera_loja'),

    path('exporta/pedido/excel/<id>', exporta_pedido_excel, name='exporta_pedido_excel'),
    path('exporta/pedidoitem/excel/<id>', exporta_pedidoitem_excel, name='exporta_pedidoitem_excel'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

