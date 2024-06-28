from django.shortcuts import render, redirect
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


