from django import forms
from app.funcionarios.models import Funcionario

class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        
    class Meta:
        model = Funcionario
        fields = '__all__'
    