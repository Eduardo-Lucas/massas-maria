import csv

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cart.cart import Cart
from cart.forms import CartAddProductForm
from faturamento.models import Participante
from materiais.filters import PedidoWebFilter
from .models import Produto, PedidoWeb, PedidoWebItem, Loja
from .forms import OrderUpdateForm, OrderCreateForm, PedidoWebForm, PedidoWebItemForm


def home(request):
    return render(request, 'materiais/produto/list.html')


"""
  TELA DE EMISSÃO DE PEDIDO TIPO E-COMMERCE
"""


class ProdutoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'materiais/produto/produto_form.html'


class ProdutoList(SuccessMessageMixin, ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'materiais/produto/list.html'

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(produto__icontains=valor) |
                Q(descricao__icontains=valor) |
                Q(preco_venda__icontains=valor) |
                Q(categoria__nome__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 12)  # Show 12 produtos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset


# @login_required
# def produto_list(request, categoria_slug=None):
#     categoria = None
#     categorias = Categoria.objects.all()
#     produtos = Produto.objects.filter(disponivel=True)
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(produtos, 10)
#     try:
#         produtos = paginator.page(page)
#     except PageNotAnInteger:
#         produtos = paginator.page(1)
#     except EmptyPage:
#         produtos = paginator.page(paginator.num_pages)
#
#     if categoria_slug:
#         categoria = get_object_or_404(Categoria, slug=categoria_slug)
#         produtos = produtos.filter(categoria=categoria)
#
#     return render(request, 'materiais/produto/list.html', {'categoria': categoria,
#                                                            'categorias': categorias,
#                                                            'produtos': produtos})


def produto_detail(request, id=None, slug=None):
    produto = get_object_or_404(Produto, id=id, slug=slug)
    cart_produto_form = CartAddProductForm(initial={'preco_negociado': produto.preco_venda})
    return render(request, 'materiais/produto/detail.html', {'produto': produto,
                                                             'cart_produto_form': cart_produto_form})

# def produto_detail(request, id=None, slug=None):
#     produto = get_object_or_404(Produto, id=id, slug=slug, disponivel=True)
#     cart_produto_form = CartAddProductForm(initial={'preco_negociado': produto.preco_venda})
#     return render(request, 'materiais/produto/detail.html', {'produto': produto,
#                                                              'cart_produto_form': cart_produto_form})
#


class ProdutoDetalhe(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'materiais/produto/produto_detail.html'


@login_required()
def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            pedidoweb = form.save(commit=False)
            
            pedidoweb.vendedor = request.user

            pedidoweb.total_produtos = cart.get_total_price()
            pedidoweb.save()

            seq = 0
            for item in cart:

                seq += 1
                PedidoWebItem.objects.create(pedidoweb=pedidoweb,
                                             sequencia=seq,
                                             produto=item['product'],
                                             unidade=item['unidade'],
                                             descricao=item['descricao'],
                                             observacoes=item['observacoes'],
                                             cfop=item['cfop'],
                                             codigo_ncm=item['codigo_ncm'],
                                             codigo_cest=item['codigo_cest'],
                                             status_pedido_item=item['status_pedido_item'],
                                             autorizacao_faturamento=item['autorizacao_faturamento'],
                                             autorizacao_numitem=item['autorizacao_numitem'],
                                             quantidade=item['quantity'],
                                             peso_liquido=item['peso_liquido'],
                                             peso_bruto=item['peso_bruto'],
                                             metro_cubico=item['metro_cubico'],
                                             movimenta_estoques=item['movimenta_estoques'],
                                             saldo_fisico=item['saldo_fisico'],
                                             saldo_fiscal=item['saldo_fiscal'],
                                             preco_custo=item['preco_custo'],
                                             preco_medio=item['preco_medio'],
                                             preco_custo_nfe=item['preco_custo_nfe'],
                                             preco_medio_nfe=item['preco_medio_nfe'],
                                             preco_unitario=item['price'],
                                             perc_desc=item['perc_desc'],
                                             custo_informado=item['custo_informado'],
                                             data_movimento=item['data_movimento'],
                                             # participante=pedidoweb.participante,
                                             total_produto=item['total_produto'],
                                             modalidade_ipi=item['modalidade_ipi'],
                                             situacao_tributaria_ipi=item['situacao_tributaria_ipi'],
                                             base_calc_ipi=item['base_calc_ipi'],
                                             perc_ipi=item['perc_ipi'],
                                             perc_red_ipi=item['perc_red_ipi'],
                                             modalidade_calculo=item['modalidade_calculo'],
                                             modalidade_icms=item['modalidade_icms'],
                                             situacao_tributaria_icms=item['situacao_tributaria_icms'],
                                             base_calc_icms=item['base_calc_icms'],
                                             perc_icms=item['perc_icms'],
                                             perc_antec_tributaria=item['perc_antec_tributaria'],
                                             perc_red_icms=item['perc_red_icms'],
                                             modalidade_calculo_subst=item['modalidade_calculo_subst'],
                                             base_calc_icms_sub=item['base_calc_icms_sub'],
                                             perc_mva_sub=item['perc_mva_sub'],
                                             perc_icms_sub=item['perc_icms_sub'],
                                             base_calc_antecipacao_trib=item['base_calc_antecipacao_trib'],
                                             perc_antecipacao_trib=item['perc_antecipacao_trib'],
                                             situacao_tributaria_pis=item['situacao_tributaria_pis'],
                                             base_calc_pis=item['base_calc_pis'],
                                             perc_pis=item['perc_pis'],
                                             situacao_tributaria_cofins=item['situacao_tributaria_cofins'],
                                             base_calc_cofins=item['base_calc_cofins'],
                                             perc_fundo_pobreza=item['perc_fundo_pobreza'],
                                             perc_trib_aproximado=item['perc_trib_aproximado'],
                                             base_calc_import=item['base_calc_import'],
                                             perc_import=item['perc_import'],
                                             base_calc_issqn=item['base_calc_issqn'],
                                             perc_issqn=item['perc_issqn'],
                                             perc_desp_acessorias=item['perc_desp_acessorias'],
                                             perc_seguro=item['perc_seguro'],
                                             perc_frete=item['perc_frete'],
                                             natureza_custos=item['natureza_custos'],
                                             centro_custo=item['centro_custo'],
                                             codigo_promocao=item['codigo_promocao']
                                             )
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request, 'materiais/pedido/created.html', {'pedidoweb': pedidoweb})
    else:
        form = OrderCreateForm()
    return render(request, 'materiais/pedido/create.html', {'cart': cart,
                                                            'form': form})


@login_required()
def order_update(request, id=None):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderUpdateForm(request.POST)

        if form.is_valid():
    
            cd = form.cleaned_data
            
            id = cd['id']
            
            pedidoweb = PedidoWeb.objects.get(id=str(id))

            seq = int(pedidoweb.maior_sequencia())
            
            for item in cart:

                seq += 1
                PedidoWebItem.objects.create(pedidoweb=pedidoweb,
                                             sequencia=seq,
                                             produto=item['product'],
                                             unidade=item['unidade'],
                                             descricao=item['descricao'],
                                             observacoes=item['observacoes'],
                                             cfop=item['cfop'],
                                             codigo_ncm=item['codigo_ncm'],
                                             codigo_cest=item['codigo_cest'],
                                             status_pedido_item=item['status_pedido_item'],
                                             autorizacao_faturamento=item['autorizacao_faturamento'],
                                             autorizacao_numitem=item['autorizacao_numitem'],
                                             quantidade=item['quantity'],
                                             peso_liquido=item['peso_liquido'],
                                             peso_bruto=item['peso_bruto'],
                                             metro_cubico=item['metro_cubico'],
                                             movimenta_estoques=item['movimenta_estoques'],
                                             saldo_fisico=item['saldo_fisico'],
                                             saldo_fiscal=item['saldo_fiscal'],
                                             preco_custo=item['preco_custo'],
                                             preco_medio=item['preco_medio'],
                                             preco_custo_nfe=item['preco_custo_nfe'],
                                             preco_medio_nfe=item['preco_medio_nfe'],
                                             preco_unitario=item['price'],
                                             perc_desc=item['perc_desc'],
                                             custo_informado=item['custo_informado'],
                                             data_movimento=item['data_movimento'],
                                             participante=pedidoweb.participante,
                                             total_produto=item['total_produto'],
                                             modalidade_ipi=item['modalidade_ipi'],
                                             situacao_tributaria_ipi=item['situacao_tributaria_ipi'],
                                             base_calc_ipi=item['base_calc_ipi'],
                                             perc_ipi=item['perc_ipi'],
                                             perc_red_ipi=item['perc_red_ipi'],
                                             modalidade_calculo=item['modalidade_calculo'],
                                             modalidade_icms=item['modalidade_icms'],
                                             situacao_tributaria_icms=item['situacao_tributaria_icms'],
                                             base_calc_icms=item['base_calc_icms'],
                                             perc_icms=item['perc_icms'],
                                             perc_antec_tributaria=item['perc_antec_tributaria'],
                                             perc_red_icms=item['perc_red_icms'],
                                             modalidade_calculo_subst=item['modalidade_calculo_subst'],
                                             base_calc_icms_sub=item['base_calc_icms_sub'],
                                             perc_mva_sub=item['perc_mva_sub'],
                                             perc_icms_sub=item['perc_icms_sub'],
                                             base_calc_antecipacao_trib=item['base_calc_antecipacao_trib'],
                                             perc_antecipacao_trib=item['perc_antecipacao_trib'],
                                             situacao_tributaria_pis=item['situacao_tributaria_pis'],
                                             base_calc_pis=item['base_calc_pis'],
                                             perc_pis=item['perc_pis'],
                                             situacao_tributaria_cofins=item['situacao_tributaria_cofins'],
                                             base_calc_cofins=item['base_calc_cofins'],
                                             perc_fundo_pobreza=item['perc_fundo_pobreza'],
                                             perc_trib_aproximado=item['perc_trib_aproximado'],
                                             base_calc_import=item['base_calc_import'],
                                             perc_import=item['perc_import'],
                                             base_calc_issqn=item['base_calc_issqn'],
                                             perc_issqn=item['perc_issqn'],
                                             perc_desp_acessorias=item['perc_desp_acessorias'],
                                             perc_seguro=item['perc_seguro'],
                                             perc_frete=item['perc_frete'],
                                             natureza_custos=item['natureza_custos'],
                                             centro_custo=item['centro_custo'],
                                             codigo_promocao=item['codigo_promocao']
                                             )
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request, 'materiais/pedido/updated.html', {})
    else:
        form = OrderUpdateForm()
    return render(request, 'materiais/pedido/update.html', {'form': form})


"""
  TELA DE EMISSÃO DE PEDIDO TIPO TRADICIONAL
"""


class PedidoWebTradicionalList(SuccessMessageMixin, LoginRequiredMixin, ListView):
    model = PedidoWeb
    template_name = 'materiais/pedido/pedidoweb_list.html'

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(participante__razao_social__icontains=valor) |
                Q(prazo_de_pagamento__descricao__icontains=valor) |
                Q(tipo_de_pagamento__descricao__icontains=valor) |
                Q(id__icontains=valor) |
                Q(observacoes__icontains=valor) |
                Q(data_pedido__icontains=valor) |
                Q(total_produtos__icontains=valor) |
                Q(status_pedido__icontains=valor)
            )
        else:
            # this returns the first 100 objects (LIMIT 100):
            if self.request.user.is_superuser:
                object_list = self.model.objects.all()[:100]
            else:
                object_list = self.model.objects.filter(vendedor=self.request.user)[:100]

        paginator = Paginator(object_list, 9)  # Show 9 pedidos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset


class PedidoWebTradicionalDetalhe(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = PedidoWeb
    context_object_name = 'pedidoweb'
    template_name = 'materiais/pedido/pedidoweb_detail.html'


def manage_pedidowebitem(request):
    PedidoWebFormSet = formset_factory(PedidoWebForm)
    PedidoWebItemFormSet = formset_factory(PedidoWebItemForm)
    if request.method == 'POST':
        pedidoweb_formset = PedidoWebFormSet(request.POST, request.FILES, prefix='pedidos')
        pedidowebitem_formset = PedidoWebItemFormSet(request.POST, request.FILES, prefix='items')
        if pedidoweb_formset.is_valid() and pedidowebitem_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            pass
    else:
        pedidoweb_formset = PedidoWebFormSet(prefix='pedidos')
        pedidowebitem_formset = PedidoWebItemFormSet(prefix='items')
    return render(request, 'materiais/pedido/manage_pedidowebitem.html', {
        'pedidoweb_formset': pedidoweb_formset,
        'pedidowebitem_formset': pedidowebitem_formset,
    })

# def manage_pedidowebitem(request, pk):
#     pedidoweb = PedidoWeb.objects.get(pk=pk)
#     if request.method == "POST":
#         formset = PedidoWebFormSet(request.POST, instance=pedidoweb)
#         if formset.is_valid():
#             formset.save()
#             # Do something. Should generally end with a redirect. For example:
#             return redirect('order_create', pedidoweb_id=pedidoweb.id)
#
#     else:
#         formset = PedidoWebFormSet(instance=pedidoweb)
#     return render(request, 'materiais/pedido/manage_pedidowebitem.html', {'formset': formset})


class PedidoWebTradicionalUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PedidoWeb
    fields = ['participante', 'tipo_de_pagamento', 'prazo_de_pagamento', ]
    template_name = 'materiais/pedido/manage_pedidowebitem.html'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.id,
        )


def search_pedidoweb(request):
    if request.user.is_superuser:
        pedidoweb_list = PedidoWeb.objects.all()
    else:
        pedidoweb_list = PedidoWeb.objects.filter(vendedor=request.user)

    pedidoweb_filter = PedidoWebFilter(request.GET, queryset=pedidoweb_list)
    return render(request, 'materiais/search_pedidoweb/pedidoweb_filter_list.html', {'filter': pedidoweb_filter})


class PedidoWebDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PedidoWeb
    success_message = 'Pedido apagado com sucesso!'
    success_url = reverse_lazy('materiais:pedidoweb_list')


class PedidoWebItemDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PedidoWebItem
    success_message = 'Item do Pedido apagado com sucesso!'
    success_url = reverse_lazy('materiais:pedidoweb_list')
    

class PedidoWebItemUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PedidoWebItem
    context_object_name = 'pedidowebitem'
    fields = ['preco_unitario', 'quantidade', 'perc_desc', ]
    template_name = 'materiais/pedidoItem/pedidowebitem_detail.html'

    success_message = 'Registro alterado com sucesso!'


# class PedidoWebItemCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     model = PedidoWebItem
#     context_object_name = 'pedidowebitem'
#     fields = ['produto', 'quantidade', 'perc_desc', ]
#     template_name = 'materiais/pedidoItem/pedidowebitem_create.html'
#
#     success_message = 'Registro criado com sucesso!'
    
def pedidowebitemcreate(request, pk):
    pedido = pk
    if request.method == 'POST':
        context = {
            'method': 'POST',
            'pedido': pedido
        }
    else:
        context = {
            'method': 'GET',
            'pedido': pedido
        }

    return render(request, 'materiais/pedidoItem/pedidowebitem_create.html',
                  {'context': context})


def expedicao(request):
    pedidos_separar = PedidoWeb.objects.filter(Q(status_pedido__startswith='e') | Q(status_pedido__startswith='w'))
    pedidos_em_separacao = PedidoWeb.objects.filter(status_pedido='s')
    pedidos_separados = PedidoWeb.objects.filter(status_pedido='t')
    
    return render(request, 'materiais/expedicao/expedicao.html',
                  {'pedidos_separar':      pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados':    pedidos_separados})


@require_POST
def inicia_separacao(request, id):
    pedido = get_object_or_404(PedidoWeb, id=id)
    pedido.status_pedido = 's'
    pedido.save()
    
    pedidos_separar = PedidoWeb.objects.filter(Q(status_pedido__startswith='e') | Q(status_pedido__startswith='w'))
    pedidos_em_separacao = PedidoWeb.objects.filter(status_pedido='s')
    pedidos_separados = PedidoWeb.objects.filter(status_pedido='t')
    
    return render(request, 'materiais/expedicao/expedicao.html',
                  {'pedidos_separar':      pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados':    pedidos_separados})


@require_POST
def finaliza_separacao(request, id):
    pedido = get_object_or_404(PedidoWeb, id=id)
    pedido.status_pedido = 't'
    pedido.save()
    
    pedidos_separar = PedidoWeb.objects.filter(Q(status_pedido__startswith='e') | Q(status_pedido__startswith='w'))
    pedidos_em_separacao = PedidoWeb.objects.filter(status_pedido='s')
    pedidos_separados = PedidoWeb.objects.filter(status_pedido='t')
    
    return render(request, 'materiais/expedicao/expedicao.html',
                  {'pedidos_separar':      pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados':    pedidos_separados})


@require_POST
def estorna_separacao(request, id):
    pedido = get_object_or_404(PedidoWeb, id=id)
    pedido.status_pedido = 'e'
    pedido.save()
    
    pedidos_separar = PedidoWeb.objects.filter(Q(status_pedido='e') | Q(status_pedido='w'))
    pedidos_em_separacao = PedidoWeb.objects.filter(status_pedido='s')
    pedidos_separados = PedidoWeb.objects.filter(status_pedido='t')
    
    return render(request, 'materiais/expedicao/expedicao.html',
                  {'pedidos_separar':      pedidos_separar,
                   'pedidos_em_separacao': pedidos_em_separacao,
                   'pedidos_separados':    pedidos_separados})


class AlteraLojaUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PedidoWeb
    fields = ['loja', ]
    context_object_name = 'pedidoweb'
    template_name = 'materiais/expedicao/altera_loja.html'


def checkout(request):
    url = "https://ws.sandbox.pagseguro.uol.com.br/v2/sessions"
    
    credenciais = {
        'email': 'eduardolucas40@gmail.com',
        'token': '9958CD2A81104D2B8DD725AEBB9BD28F'
    }
    
    headers = {'user-agent': 'my-app/0.0.1'}
    
    session_id = requests.post(url, params=credenciais)
    
    return render(request, 'materiais/checkout/checkout.html', {'session_id': session_id})


def exporta_pedido_csv(request, id=0):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedido.csv"'

    writer = csv.writer(response)
    writer.writerow(['Numero', 'Data do Pedido', 'Cliente', 'vendedor'])

    pedidos = PedidoWeb.objects.filter(id=id).values_list('id', 'data_pedido', 'participante', 'vendedor')
    for pedido in pedidos:
        writer.writerow(pedido)

    return response
