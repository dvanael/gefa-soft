from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/create.html"
    success_url = reverse_lazy("list-produtos")


class ProdutoDeleteView(DeleteView):
    model = Produto
    context_object_name = "produto"
    template_name = "Produtos/delete.html"
    success_url = reverse_lazy("list-produtos")


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/update.html"
    success_url = reverse_lazy("list-produtos")


class ProdutoListView(ListView):
    model = Produto
    context_object_name = "produtos"
    template_name = "produtos/list.html"
