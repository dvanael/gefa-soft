from django import forms
from decimal import Decimal, InvalidOperation
from app.insumos.models import Insumo

class InsumoForm(forms.ModelForm):
    preco = forms.CharField(label='Preço')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control price'})
            
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