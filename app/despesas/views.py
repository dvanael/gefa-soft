from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import GastoInsumo
from .forms import GastoInsumoForm


class GastoInsumoListView(ListView):
    model = GastoInsumo
    template_name = 'despesas/insumos/list.html'
    context_object_name = 'gastos_insumo'

class GastoInsumoCreateView(CreateView):
    model = GastoInsumo
    form_class = GastoInsumoForm
    template_name = 'despesas/insumos/create.html'
    success_url = reverse_lazy('list-gasto-insumo')

class GastoInsumoDeleteView(DeleteView):
    model = GastoInsumo
    template_name = 'despesas/insumos/delete.html'
    success_url = reverse_lazy('list-gasto-insumo')

class GastoInsumoUpdateView(UpdateView):
    model = GastoInsumo
    form_class = GastoInsumoForm
    template_name = 'despesas/insumos/update.html'
    success_url = reverse_lazy('list-gasto-insumo')