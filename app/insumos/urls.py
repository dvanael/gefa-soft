from django.urls import path
from app.insumos.views import (
    InsumoListView,
    InsumoCreateView,
    InsumoDeleteView,
    InsumoUpdateView,
)

urlpatterns = [
    path("", InsumoListView.as_view(), name="list-insumos"),
    path("cadastrar", InsumoCreateView.as_view(), name="create-insumo"),
    path("<int:pk>/atualizar/", InsumoUpdateView.as_view(), name="update-insumo"),
    path("deletar/<int:pk>/", InsumoDeleteView.as_view(), name="delete-insumo"),
]
