from firedrake import *

gridseq = False  # if True, use coarse solution as next initial iterate

mesh0 = RectangleMesh(15, 15, 2, 2, -2, -2, diagonal="crossed")
hierarchy = MeshHierarchy(mesh0, 4)  # m = 15, 30, 60, 120, 240
uh = None
for mesh in hierarchy:
    x, y = SpatialCoordinate(mesh)
    r2 = x ** 2 + y ** 2
    V = FunctionSpace(mesh, "P", 1)
    psih = Function(V).interpolate(conditional(r2 < 1, sqrt(1 - r2), 0))
    uold = uh
    uh, vh = Function(V), TestFunction(V)
    if gridseq and uold is not None:
        prolong(uold, uh)
    F = inner(grad(uh), grad(vh)) * dx
    bcs = DirichletBC(V, Constant(0.0), "on_boundary")
    prob = NonlinearVariationalProblem(F, uh, bcs)
    sp = {"snes_type": "vinewtonrsls"}
    solver = NonlinearVariationalSolver(prob, solver_parameters=sp)
    INF = Function(V).interpolate(Constant(PETSc.INFINITY))
    solver.solve(bounds=(psih, INF))
    m = int(round(sqrt(mesh.num_cells() / 4)))
    q = solver.snes.getIterationNumber()
    print(f"{m:4d} x {m:4d}: {q} Newton iterations")
