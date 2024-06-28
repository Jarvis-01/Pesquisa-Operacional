# views.py em produtos app
from django.shortcuts import render, redirect

from materiaPrima.models import MateriaPrima
from .forms import ProdutoForm, ProdutoMateriaPrimaForm
from .models import Produto, ProdutoMateriaPrima

def adicionar(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save()
            for materia_prima_id in request.POST.getlist('materia_prima'):
                quantidade = request.POST.get('quantidade_' + materia_prima_id)
                if quantidade:  # Verifica se a quantidade não está vazia
                    ProdutoMateriaPrima.objects.create(
                        produto=produto,
                        materia_prima_id=materia_prima_id,
                        quantidade=quantidade
                    )
            return redirect('../')
    else:
        produto_form = ProdutoForm()
        materia_prima_form = ProdutoMateriaPrimaForm()

    context = {
        'produto_form': produto_form,
        'materia_prima_form': materia_prima_form,
        'materias_primas': MateriaPrima.objects.all()
    }
    return render(request, 'adicionar_produto.html', context)

def index(request):
    produto = Produto.objects.all()
    context = {
        'lista': produto
    }
    return render(request, 'produtos.html', context)