from django.urls import path
from app.funcionarios.views import FuncionarioCreateView, FuncionarioDeleteView, FuncionarioListView, FuncionarioUpdateView

urlpatterns = [
    path('funcionarios/', FuncionarioListView.as_view(), name='list-funcionarios'),
    path('funcionarios/cadastrar', FuncionarioCreateView.as_view(), name='create-funcionario'),
    path('funcionarios/<int:pk>/deletar', FuncionarioDeleteView.as_view(), name='delete-funcionario'),
    path('funcionarios/<int:pk>/atualizar', FuncionarioUpdateView.as_view(), name='update-funcionario'),
]