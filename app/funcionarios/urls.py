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
    path("funcionarios/", FuncionarioListView.as_view(), name="list-funcionarios"),
    path(
        "funcionarios/cadastrar",
        FuncionarioCreateView.as_view(),
        name="create-funcionario",
    ),
    path(
        "funcionarios/<int:pk>/deletar",
        FuncionarioDeleteView.as_view(),
        name="delete-funcionario",
    ),
    path(
        "funcionarios/<int:pk>/atualizar/",
        FuncionarioUpdateView.as_view(),
        name="update-funcionario",
    ),
    # PRODUÇÃO
    path("funcionarios/<int:pk>/produções/", list_producao, name="list-producao"),
    path(
        "funcionarios/<int:pk>/produções/cadastrar/",
        create_producao,
        name="create-producao",
    ),
    path(
        "funcionarios/<int:pk>/produções/<int:producao_pk>/atualizar/",
        update_producao,
        name="update-producao",
    ),
    path(
        "funcionarios/<int:pk>/produções/<int:producao_pk>/deletar/",
        delete_producao,
        name="delete-producao",
    ),
]
