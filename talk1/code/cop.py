from firedrake import *

mesh = RectangleMesh(30, 30, 2, 2, -2, -2, diagonal="crossed")
x, y = SpatialCoordinate(mesh)
r2 = x ** 2 + y ** 2
psi = conditional(r2 < 1, sqrt(1 - r2), 0)

V = FunctionSpace(mesh, "P", 1)
psih = Function(V, name="psi_h").interpolate(psi)
uh = Function(V, name="u_h")
vh = TestFunction(V)
F = inner(grad(uh), grad(vh)) * dx  # f = 0
bcs = DirichletBC(V, Constant(0.0), "on_boundary")  # g = 0
problem = NonlinearVariationalProblem(F, uh, bcs)

sp = {"snes_type": "vinewtonrsls",  # <- explained next week
      "snes_converged_reason": None}  # 6 iterations for *this* grid
solver = NonlinearVariationalSolver(problem, solver_parameters=sp)
INF = Function(V).interpolate(Constant(PETSc.INFINITY))
solver.solve(bounds=(psih, INF))
VTKFile("cop.pvd").write(uh, psih)
