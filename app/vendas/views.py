from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from app.vendas.models import Venda, ProdutoVenda
from app.vendas.forms import VendaForm, ProdutoVendaForm, ProdutoVendaFormSet
from django.views.generic import CreateView, DeleteView, UpdateView, ListView


class VendaCreateView(CreateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/create.html"
    success_url = reverse_lazy("list-vendas")


class VendaDeleteView(DeleteView):
    model = Venda
    template_name = "vendas/delete.html"
    success_url = reverse_lazy("list-vendas")


class VendaUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/update.html"
    success_url = reverse_lazy("list-vendas")


class VendaListView(ListView):
    model = Venda
    template_name = "vendas/list.html"
    context_object_name = "vendas"


def list_produto_venda(request, pk):
    template_name = "vendas/produtos/list.html"
    context = {}

    venda = get_object_or_404(Venda, pk=pk)
    produtos = ProdutoVenda.objects.filter(venda=venda)

    context["venda"] = venda
    context["produtos"] = produtos

    return render(request, template_name, context)


def update_produto_venda(request, pk, produto_venda_pk):
    template_name = "vendas/produtos/update.html"
    context = {}

    venda = get_object_or_404(Venda, pk=pk)
    context["venda"] = venda

    produto_venda = get_object_or_404(ProdutoVenda, pk=produto_venda_pk)
    context["produto_venda"] = produto_venda

    if request.method == "POST":
        form = ProdutoVendaForm(request.POST, instance=produto_venda)
        if form.is_valid():
            form.save()
            return redirect("list-produto-venda", pk)

    form = ProdutoVendaForm(instance=produto_venda)
    context["form"] = form
    return render(request, template_name, context)


def delete_produto_venda(request, pk, produto_venda_pk):
    template_name = "vendas/produtos/delete.html"
    context = {}

    venda = get_object_or_404(Venda, pk=pk)
    context["venda"] = venda

    produto_venda = get_object_or_404(ProdutoVenda, pk=produto_venda_pk)
    context["produto_venda"] = produto_venda

    if request.method == "POST":
        produto_venda.delete()
        return redirect("list-produto-venda", pk)

    return render(request, template_name, context)


def create_venda(request):
    template_name = "vendas/create.html"
    context = {}

    form = VendaForm()
    form_produto_venda = ProdutoVendaFormSet()

    context["form"] = form
    context["form_produto_venda"] = form_produto_venda

    if request.method == "POST":
        form = VendaForm(request.POST)
        form_produto_venda = ProdutoVendaFormSet(request.POST)

        if form.is_valid() and form_produto_venda.is_valid():
            venda = form.save()
            form_produto_venda.instance = venda
            form_produto_venda.save()

        return redirect("list-vendas")

    return render(request, template_name, context)
