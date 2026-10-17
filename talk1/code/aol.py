from firedrake import *

mesh = RectangleMesh(6, 12, 0.5, 1.0)
x, y = SpatialCoordinate(mesh)
r2 = (x + 1.0) ** 2 + y ** 2
g = conditional(r2 < 2.0, 0.25 * r2 - 0.5 - 0.5 * ln(0.5 * r2), 0.0)

V = FunctionSpace(mesh, "CG", 1)
uh, vh = Function(V, name="u_h"), TestFunction(V)
F = inner(grad(uh), grad(vh)) * dx - Constant(-1) * vh * dx
bcs = DirichletBC(V, Function(V).interpolate(g), "on_boundary")
problem = NonlinearVariationalProblem(F, uh, bcs)

sp = {"snes_type": "vinewtonrsls"}
solver = NonlinearVariationalSolver(problem, solver_parameters=sp)
