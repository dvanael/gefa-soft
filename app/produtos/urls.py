from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoDeleteView,
    ProdutoUpdateView,
)

urlpatterns = [
    path("", ProdutoListView.as_view(), name="list-produtos"),
    path("cadastrar/", ProdutoCreateView.as_view(), name="create-produto"),
    path(
        "<int:pk>/atualizar/",
        ProdutoUpdateView.as_view(),
        name="update-produto",
    ),
    path("<int:pk>/deletar/", ProdutoDeleteView.as_view(), name="delete-produto"),
]
