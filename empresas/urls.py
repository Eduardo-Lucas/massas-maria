from django.urls import path

from empresas.views import *
app_name = 'empresas'
urlpatterns = [
    path('list/', EmpresaListView.as_view(), name='empresa_list'),
    path('create/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('update/<str:pk>', EmpresaUpdateView.as_view(), name='empresa_update'),

    path('tabelaprecoitem_list/', TabelaPrecoItemListView.as_view(), name='tabelaprecoitem_list'),

]
