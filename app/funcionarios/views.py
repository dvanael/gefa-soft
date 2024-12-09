from django.shortcuts import render
from app.funcionarios.models import Funcionario
from app.funcionarios.forms import FuncionarioForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/create.html'
    success_url = reverse_lazy('list-funcionarios')
    
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/delete.html'
    success_url = reverse_lazy('list-funcionarios')
    
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionarios/update.html'
    success_url = reverse_lazy('list-funcionarios')
    
class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'funcionarios/list.html'
    context_object_name = 'funcionarios'
