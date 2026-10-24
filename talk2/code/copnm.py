# solve a classical obstacle problem using a Newton-multigrid approach
# note: Newton = vinewtonrsls, an active-set method
#       multigrid = linear geometric multigrid on the assembled linear systems

from firedrake import *
import patch_vi_mg  # fix-up prolongation matrix (P) and coarse caching issues
import time

MG_SOLVER = False  # if False, uses MUMPS direct solve on linear systems

mesh0 = RectangleMesh(10, 10, 2, 2, -2, -2, diagonal="crossed")
hierarchy = MeshHierarchy(mesh0, 5)
uh = None
for mesh in hierarchy:
    x, y = SpatialCoordinate(mesh)
    r2 = x ** 2 + y ** 2
    V = FunctionSpace(mesh, "P", 1)
    psih = Function(V).interpolate(conditional(r2 < 1, sqrt(1 - r2), 0))
    f = Function(V).interpolate(sin(20*(x+y**2)))  # more interesting active set
    # f = Constant(0.0)  # boring active set
    uold = uh
    uh, vh = Function(V), TestFunction(V)
    if uold is not None:
        prolong(uold, uh)  # grid sequencing
    F = inner(grad(uh), grad(vh)) * dx - 10 * f * vh * dx
    bcs = DirichletBC(V, Constant(0.0), "on_boundary")
    prob = NonlinearVariationalProblem(F, uh, bcs)
    sp = {"snes_type": "vinewtonrsls",
          "snes_converged_reason": None}
    if MG_SOLVER:
        # note this is SERIAL ONLY; for parallel, either:
        #    1. -mg_levels_pc_type bjacobi -mg_levels_sub_pc_type icc  (and fix prints)
        #    2. switch to FASCD
        sp.update({
            "ksp_type": "cg",
            "ksp_converged_reason": None,
            "pc_type": "mg",
            "mg_levels_ksp_type": "chebyshev",
            "mg_levels_ksp_max_it": 2,
            "mg_levels_pc_type": "icc",
            #"mg_levels_ksp_converged_reason": None,
            })
    solver = NonlinearVariationalSolver(prob, solver_parameters=sp, options_prefix="s")
    INF = Function(V).interpolate(Constant(PETSc.INFINITY))
    t0 = time.perf_counter()
    solver.solve(bounds=(psih, INF))
    dt = time.perf_counter() - t0
    m = int(round(sqrt(mesh.num_cells() / 4)))
    q = solver.snes.getIterationNumber()
    print(f"{m:4d} x {m:4d}: {q} Newton iterations, solve {dt:.2f} s")

uh.rename("uh")
psih.rename("psih")
active = Function(V, name="active").interpolate(conditional(uh - psih > 1.0e-8, 0.0, 1.0))
VTKFile(f"result.pvd").write(uh, psih, active)
