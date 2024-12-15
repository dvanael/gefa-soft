from django import forms
from app.funcionarios.models import Funcionario, Producao


class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)

    class Meta:
        model = Funcionario
        fields = "__all__"


class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = ("produto", "quantidade", "data")
        widgets = {
            "data": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date", "class": "form-control"}
            ),
        }
