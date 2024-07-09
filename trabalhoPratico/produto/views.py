# views.py em produtos app
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

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
                quantidade = float(quantidade.replace(',', '.'))
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

def detalhes(request,produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto_materia_prima = ProdutoMateriaPrima.objects.filter(produto=produto)
    print("Lista de materias-primas do produto: {}".format(produto_materia_prima))

    context = {
        'produto': produto,
        'produto_materia_Prima': produto_materia_prima
    }
    return render(request, 'detalhes.html', context)

def editar(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(instance=produto)

    if(request.method == 'POST'):
        form = ProdutoForm(request.POST, instance=produto)

        if(form.is_valid()):
            produto.save()
            return redirect('../')
        else:
            return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

    else:
        return render(request, 'editar_produto.html', {'form': form, 'produto': produto})
    
def deletar(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('../')