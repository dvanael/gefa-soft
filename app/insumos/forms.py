from django import forms
from app.insumos.models import TipoInsumo, Insumo

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'
        