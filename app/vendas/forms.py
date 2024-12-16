from django import forms
from app.vendas.models import Venda, ProdutoVenda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget = forms.DateInput(format=("%Y-%m-%d"), attrs={"type": "date", "class": "form-control"})
        
class ProdutoVendaForm(forms.ModelForm):
    class Meta:
        model = ProdutoVenda
        fields = '__all__'