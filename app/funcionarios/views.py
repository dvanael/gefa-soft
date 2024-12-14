from django.shortcuts import render, get_object_or_404, redirect
from app.funcionarios.models import Funcionario, Producao
from app.funcionarios.forms import FuncionarioForm, ProducaoForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy


class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/create.html"
    success_url = reverse_lazy("list-funcionarios")


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "funcionarios/delete.html"
    success_url = reverse_lazy("list-funcionarios")


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/update.html"
    success_url = reverse_lazy("list-funcionarios")


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "funcionarios/list.html"
    context_object_name = "funcionarios"


def list_producao(request, pk):
    template = "funcionarios/producao/list.html"
    context = {}

    funcionario = Funcionario.objects.get(pk=pk)
    producoes = Producao.objects.filter(funcionario=funcionario)

    context["funcionario"] = funcionario
    context["producoes"] = producoes
    return render(request, template, context)


def create_producao(request, pk):
    template = "funcionarios/producao/create.html"
    context = {}

    funcionario = get_object_or_404(Funcionario, pk=pk)
    context["funcionario"] = funcionario

    if request.method == "POST":
        form = ProducaoForm(request.POST)
        if form.is_valid():
            form.instance.funcionario = funcionario
            form.save()
        return redirect("list-producao", pk)

    elif request.method == "GET":
        form = ProducaoForm()

    context["form"] = form
    return render(request, template, context)


def update_producao(request, pk, producao_pk):
    template = "funcionarios/producao/update.html"
    context = {}

    producao = get_object_or_404(Producao, producao_pk)
    context["producao"] = producao

    funcionario = get_object_or_404(Funcionario, pk=pk)
    context["funcionario"] = funcionario

    if request.method == "POST":
        form = ProducaoForm(request.POST, instance=producao)
        if form.is_valid():
            form.save()
        return redirect("list-producao", pk)

    elif request.method == "GET":
        form = ProducaoForm(instance=producao)

    context["form"] = form
    return render(request, template, context)


def delete_producao(request, pk, producao_pk):
    template = "funcionarios/producao/delete.html"
    context = {}

    producao = get_object_or_404(Producao, pk=producao_pk)
    context["producao"] = producao

    funcionario = get_object_or_404(Funcionario, pk=pk)
    context["funcionario"] = funcionario

    if request.method == "POST":
        producao.delete()
        return redirect("list-producao", pk)

    return render(request, template, context)
