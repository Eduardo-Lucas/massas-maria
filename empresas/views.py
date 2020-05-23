from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from empresas.form import EmpresaForm
from empresas.models import Empresa, TabelaPrecoItem


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = '__all__'
    template_name = 'empresas/empresa_form.html'


class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    context_object_name = 'empresas'
    template_name = 'empresas/empresa_list.html'


class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    context_object_name = 'empresas'
    template_name = 'empresas/empresa_form.html'


class TabelaPrecoItemListView(LoginRequiredMixin, ListView):
    model = TabelaPrecoItem
    context_object_name = 'tabelaprecoitens'
    template_name = 'empresas/tabelaprecoitem_list.html'
