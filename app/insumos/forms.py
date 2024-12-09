from django import forms
from decimal import Decimal, InvalidOperation
from app.insumos.models import TipoInsumo, Insumo

class InsumoForm(forms.ModelForm):
    preco = forms.CharField(label='Preço',widget=forms.TextInput(attrs={'class': 'form-control price',}))
    class Meta:
        model = Insumo
        fields = '__all__'
    
    def clean_preco(self):
        data = self.cleaned_data['preco']
        data = data.replace(',', '.')
        try:
            return Decimal(data)
        except InvalidOperation:
            raise forms.ValidationError("O preço deve ser um número válido.") 
        
        
    

        