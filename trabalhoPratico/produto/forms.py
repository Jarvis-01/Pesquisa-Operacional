from django import forms
from .models import Produto, ProdutoMateriaPrima
from materiaPrima.models import MateriaPrima

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao']

class ProdutoMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = ProdutoMateriaPrima
        fields = ['materia_prima', 'quantidade']
