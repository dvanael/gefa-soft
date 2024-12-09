from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from app.insumos.models import Insumo
from app.insumos.forms import InsumoForm


# def list_insumos(request):
#     template_name = 'insumos/list.html'
#     context = {
#         'insumos': Insumo.objects.all()
#     }
#     return render(request, template_name, context)

class InsumoListView(ListView):
    model = Insumo
    template_name = 'insumos/list.html'
    context_object_name = 'insumos'
    
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