from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from . models import MateriaPrima
from . forms import MateriaPrimaForm

# Create your views here.
data = ''
def index(request):
    materiaPrima = MateriaPrima.objects.all()
    context = {
        'lista': materiaPrima
    }
    return render(request, 'materiaPrima.html', context)

def adicionar(request):
    form = MateriaPrimaForm()
    if request.method == "POST":
        form = MateriaPrimaForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = MateriaPrimaForm()
            return redirect('../')
        else:
            form = MateriaPrimaForm()
    return render(request, 'adicionar_materiaPrima.html', {'form': form})


def editar(request, id):
    materiaPrima = get_object_or_404(MateriaPrima, pk=id)
    form = MateriaPrimaForm(instance=materiaPrima)

    if(request.method == 'POST'):
        form = MateriaPrimaForm(request.POST, instance=materiaPrima)

        if(form.is_valid()):
            materiaPrima.save()
            return redirect('../')
        else:
            return render(request, 'editar_materiaPrima.html', {'form': form, 'materiaPrima': materiaPrima})

    else:
        return render(request, 'editar_materiaPrima.html', {'form': form, 'materiaPrima': materiaPrima})
    
def detalhe(request,pk):
    print("Primary Key {}".format(pk))
    try:
        materiasPrimas = MateriaPrima.objects.filter(pk=pk)
        print(materiasPrimas.values())
        
    except materiasPrimas.DoesNotExist:
        raise Http404('Falha Não Existe')
    # consulta
    context = {
        'materiasPrimas': materiasPrimas
    }
    return render(request, 'detalhe.html', context)

def deletar(request, id):
    materiaPrima = get_object_or_404(MateriaPrima, pk=id)
    materiaPrima.delete()
    return redirect('../')