from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from app.insumos.models import Insumo
from app.insumos.forms import InsumoForm
from babel.numbers import format_currency

class InsumoListView(ListView):
    model = Insumo
    template_name = 'insumos/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        insumos = Insumo.objects.all()
        insumos_formatados = []

        # Formata insumos
        for insumo in insumos:
            insumos_formatados.append({
                'pk': insumo.pk,
                'tipo': insumo.tipo,
                'preco': format_currency(insumo.preco, currency='BRL', locale='pt_BR')
            })
        context['insumos'] = insumos_formatados
        return context
    
class InsumoCreateView(CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'insumos/create.html'
    success_url = reverse_lazy('list-insumos')
    
class InsumoDeleteView(DeleteView):
    model = Insumo
    template_name = 'insumos/delete.html'
    success_url = reverse_lazy('list-insumos')
    
class InsumoUpdateView(UpdateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'insumos/update.html'
    success_url = reverse_lazy('list-insumos')