from django.urls import path
from app.funcionarios.views import (
    FuncionarioCreateView,
    FuncionarioDeleteView,
    FuncionarioListView,
    FuncionarioUpdateView,
    # PRODUÇÃO
    list_producao,
    create_producao,
    update_producao,
    delete_producao,
)

urlpatterns = [
    path("", FuncionarioListView.as_view(), name="list-funcionarios"),
    path(
        "cadastrar",
        FuncionarioCreateView.as_view(),
        name="create-funcionario",
    ),
    path(
        "<int:pk>/deletar",
        FuncionarioDeleteView.as_view(),
        name="delete-funcionario",
    ),
    path(
        "<int:pk>/atualizar/",
        FuncionarioUpdateView.as_view(),
        name="update-funcionario",
    ),
    # PRODUÇÃO
    path("<int:pk>/producoes/", list_producao, name="list-producao"),
    path(
        "<int:pk>/producoes/cadastrar/",
        create_producao,
        name="create-producao",
    ),
    path(
        "<int:pk>/producoes/<int:producao_pk>/atualizar/",
        update_producao,
        name="update-producao",
    ),
    path(
        "<int:pk>/producoes/<int:producao_pk>/deletar/",
        delete_producao,
        name="delete-producao",
    ),
]
