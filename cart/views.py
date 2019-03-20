from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from materiais.models import Produto
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        if cd['update'] is False:
                cart.add(produto=produto,
                         quantity=cd['quantity'],
                         preco_negociado=0,
                         update_quantity=cd['update'],
                         desconto=0)
                messages.success(request, 'Produto ' + produto.produto + ' ' + produto.descricao +
                                 ' colocado no carrinho.')
        else:
            cart.add(produto=produto,
                     quantity=cd['quantity'],
                     preco_negociado=0,
                     update_quantity=cd['update'],
                     desconto=0)

    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, produto_id):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=produto_id)
    cart.remove(produto)
    messages.success(request, 'Produto ' + produto.produto + ' ' + produto.descricao + ' removido do carrinho.')

    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'preco_negociado': item['preco_unitario'],
                     'update': True,
                     'perc_desc':
                         100.00 - ((float(item['preco_unitario'])*100)/float(item['price'])),
                     # 'perc_desc': item['perc_desc'],
                     'valor_desconto':
                     (item['price'] * (item['perc_desc']/100)) *
                     item['quantity']
                     })
    return render(request, 'cart/detail.html', {'cart': cart})
