from django.urls import path
from app.insumos.views import list_insumos

urlpatterns = [
    path('insumos/', list_insumos, name='list-insumos'),
]