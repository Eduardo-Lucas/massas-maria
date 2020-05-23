from django.conf.urls import url
from django.urls import path

from faturamento import api_views
from faturamento.views import *

app_name = 'faturamento'

urlpatterns = [

    # Participante
    url(r'^participante_list/$', ParticipanteList.as_view(), name='participante_list'),
    url(r'^participante_list/(?P<pk>[0-9]+)/$', ParticipanteDetalhe.as_view(), name='participante_detail'),
    url(r'^participante_add/$', ParticipanteCreate.as_view(), name='participante_add'),
    url(r'^participante/(?P<pk>[0-9]+)/edit/$', ParticipanteUpdate.as_view(), name='participante_edit'),
    url(r'^participante/(?P<id>[0-9]+)/delete/$', participante_delete, name='participante_delete'),

    path('pedido_por_cliente/<int:cliente_id>/', pedido_por_cliente, name='pedido_por_cliente'),
    path('pedido_novo_por_cliente/<int:cliente_id>/', pedido_novo_por_cliente, name='pedido_novo_por_cliente'),


]
