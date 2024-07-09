from ortools.linear_solver import pywraplp

def test_solver():
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        print("Solver não foi criado.")
        return

    x = solver.IntVar(0.0, solver.infinity(), "x")
    y = solver.IntVar(0.0, solver.infinity(), "y")
    solver.Add(x + y <= 10)
    solver.Maximize(x + y)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solução ótima encontrada.")
        print("x =", x.solution_value())
        print("y =", y.solution_value())
    else:
        print("Não foi possível encontrar uma solução ótima.")

test_solver()
