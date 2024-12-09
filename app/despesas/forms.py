from django import forms
from decimal import Decimal, InvalidOperation
from .models import GastoInsumo

class GastoInsumoForm(forms.ModelForm):
    class Meta:
        model = GastoInsumo
        fields = '__all__'

        
    

        