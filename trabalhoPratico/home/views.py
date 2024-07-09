from django.shortcuts import render
from ortools.linear_solver import pywraplp
from materiaPrima.models import MateriaPrima
from produto.models import Produto, ProdutoMateriaPrima

def index(request):
    if request.method == 'POST':
        try:
            orcamento = float(request.POST.get('orcamento'))
        except (TypeError, ValueError):
            return render(request, 'index.html', {'error': 'Orçamento inválido.'})
    else:
        return render(request, 'index.html')

    # Buscando produtos e matérias-primas do banco de dados
    produtos = Produto.objects.all()
    try:
        gabardine = MateriaPrima.objects.get(nome='Gabardine Sublimado')
    except MateriaPrima.DoesNotExist:
        return render(request, 'index.html', {'error': 'Matéria-prima Gabardine Sublimado não encontrada.'})

    # Criando o Solver
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return render(request, 'index.html', {'error': 'Solver não foi criado.'})

    # Definição das variáveis de decisão para cada produto
    variaveis = {}
    for produto in produtos:
        variaveis[produto.id] = solver.IntVar(0.0, solver.infinity(), str(produto))

    # Restrições
    restricao_orcamento = solver.Constraint(0, orcamento)
    for produto in produtos:
        custo_total_produto = sum(float(pm.materia_prima.preco) * float(pm.quantidade) for pm in ProdutoMateriaPrima.objects.filter(produto=produto)) + float(produto.mao_de_obra)
        restricao_orcamento.SetCoefficient(variaveis[produto.id], custo_total_produto)

    # Restrição adicional para limitar a quantidade de gabardine a 50 unidades
    restricao_gabardine = solver.Constraint(0, 50)
    for pm in ProdutoMateriaPrima.objects.filter(materia_prima=gabardine):
        restricao_gabardine.SetCoefficient(variaveis[pm.produto.id], pm.quantidade)

    # Função Objetivo: Maximização do Lucro
    objective = solver.Objective()
    for produto in produtos:
        custo_total_produto = sum(float(pm.materia_prima.preco) * float(pm.quantidade) for pm in ProdutoMateriaPrima.objects.filter(produto=produto)) + float(produto.mao_de_obra)
        lucro_por_unidade = float(produto.precoVenda) - custo_total_produto
        objective.SetCoefficient(variaveis[produto.id], lucro_por_unidade)
    objective.SetMaximization()

    # Resolvendo o problema
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        result = {
            'objective_value': solver.Objective().Value(),
            'variaveis': {produto.nome: variaveis[produto.id].solution_value() for produto in produtos},
            'wall_time': solver.wall_time(),
            'iterations': solver.iterations()
        }
    else:
        result = {'error': 'O problema não tem solução ótima'}

    return render(request, 'index.html', result)
