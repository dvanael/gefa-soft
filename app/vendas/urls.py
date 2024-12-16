from django.urls import path
from app.vendas.views import ( VendaCreateView, 
                              VendaDeleteView, 
                              VendaUpdateView, 
                              VendaListView, 
                              list_produto_venda, 
                              update_produto_venda, 
                              delete_produto_venda,
                            )

urlpatterns = [
  # VENDAS
  path('', VendaListView.as_view(), name='list-vendas'),
  path('cadastrar/', VendaCreateView.as_view(), name='create-venda'),
  path('<int:pk>/deletar', VendaDeleteView.as_view(), name='delete-venda'),
  path('<int:pk>/atualizar', VendaUpdateView.as_view(), name='update-venda'),
  
  # PRODUTOS
  path('<int:pk>/produtos/', list_produto_venda, name='list-produto-venda'),
  path('<int:pk>/produtos/<int:produto_venda_pk>/atualizar', update_produto_venda, name='update-produto-venda'),
  path('<int:pk>/produtos/<int:produto_venda_pk>/deletar', delete_produto_venda, name='delete-produto-venda'),
]