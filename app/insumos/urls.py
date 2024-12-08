from django.urls import path
from app.insumos.views import InsumoListView, InsumoCreateView, InsumoDeleteView, InsumoUpdateView

urlpatterns = [
    path('insumos/', InsumoListView.as_view(), name='list-insumos'),
    path('insumo/cadastrar', InsumoCreateView.as_view(), name='create-insumo'),
    path('insumo/<int:pk>/atualizar/', InsumoUpdateView.as_view(), name='update-insumo'),
    path('insumo/deletar/<int:pk>/', InsumoDeleteView.as_view(), name='delete-insumo'),
]