from django import forms
from django.forms import ModelForm
from . models import MateriaPrima

class MateriaPrimaForm(ModelForm):
    class Meta:
        model = MateriaPrima
        fields = "__all__"
