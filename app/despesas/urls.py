from django.urls import path
from .views import GastoInsumoCreateView, GastoInsumoDeleteView, GastoInsumoListView, GastoInsumoUpdateView

urlpatterns = [
    path('insumos/', GastoInsumoListView.as_view(), name='list-gasto-insumo'),
    path('insumos/cadastrar/', GastoInsumoCreateView.as_view(), name='create-gasto-insumo'),
    path('insumos/<int:pk>/atualizar/', GastoInsumoUpdateView.as_view(), name='update-gasto-insumo'),
    path('insumos/<int:pk>/deletar/', GastoInsumoDeleteView.as_view(), name='delete-gasto-insumo'),
]