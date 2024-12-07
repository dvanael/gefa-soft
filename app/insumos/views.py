from django.shortcuts import render
from app.insumos.models import Insumo

def list_insumos(request):
    template_name = 'insumos/list.html'
    context = {
        'insumos': Insumo.objects.all()
    }
    return render(request, template_name, context)
