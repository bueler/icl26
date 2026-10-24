# workarounds for SNESVINEWTONRSLS + PCMG with Firedrake DMs
import firedrake.mg.ufl_utils as uu
import firedrake.dmhooks as dh

# 1. RSLS restricts P via MatCreateSubMatrix; needs assembled (AIJ) P for Galerkin PtAP
#    assemble it by cross-mesh interpolation (no bcs, but boundary nodes are active);
#    P is fixed, so build it once per level pair
from firedrake.preconditioners.pmg import prolongation_matrix_aij

_Pcache = {}
def create_interpolation_aij(dmc, dmf):
    V_c = uu.get_appctx(dmc)._problem.u_restrict.function_space()
    V_f = uu.get_appctx(dmf)._problem.u_restrict.function_space()
    key = (V_c.mesh(), V_c.ufl_element(), V_f.mesh(), V_f.ufl_element())
    if key not in _Pcache:
        _Pcache[key] = prolongation_matrix_aij(V_c, V_f)
    return _Pcache[key], None
uu.create_interpolation = create_interpolation_aij

# 2. Firedrake caches coarse DMs, so VI marking from previous Newton step persists;
#    strip it (= DMDestroyVI) before DMCoarsen_SNESVI re-marks it
_orig_coarsen = dh.coarsen
def coarsen_clean(dm, comm):
    cdm = _orig_coarsen(dm, comm)
    cdm.compose("VI", None)
    return cdm
dh.coarsen = coarsen_clean
