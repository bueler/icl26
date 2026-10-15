# icl26

I will give a series of four applied/computational mathematical lectures at Imperial College London, in October and November of 2026.

This repository contains the slides for lectures 1 and 2.  Links to PDFs and sources for lectures 3 and 4 are also given below.  The slides themselves, and the demonstration codes they mention, are all open source, and the repository has a generous MIT license.  Please re-use as much LaTeX, Tikz, and Python as you want, ideally giving me credit as you go.

## abstract for the series

This four-lecture series introduces variational inequalities to a general applied mathematical audience, pursues their finite element solution, and applies them to a geophysical problem.  Variational inequalities are partial differential equation weak forms, but subject to bounds on their solution(s).  They reformulate how one might pose boundary conditions at a free location; where the conditions apply is now determined simultaneously along with the solution.  Certain variational inequalities state the KKT conditions of optimization problems in function spaces, and in all cases these continuum models introduce admissibility and complementarity concerns into numerical solver methodology.  Examples of variational inequalities include the classical obstacle problem, the problem of elastic contact, and, as I will emphasize, the problem of finding the extent of glaciation in a time- and space-varying climate.  Recent results and open problems will appear, regarding multigrid approaches, adaptive mesh refinement, higher-order elements, and well-posedness of the glacier model.

## lecture 1: Introduction to variational inequalities and their finite element solution

See [talk1/talk1.pdf](talk1/talk1.pdf).  All LaTeX sources for this talk are in [talk1/](talk1/).

FIXME outline:

1. Finite-dimensional examples (geometry of VIs)
  * calc 1 problem
  * projection to a closed convex set in a Hilbert space
  * extends F=0 to always have a solution or support plane
  * uniqueness, monotonicity, convex objective
2. Infinite-dimensional examples (applications of VIs)
  * classical obstacle problem
  * Signorini
  * multiple solutions (and deflation)
  * fluid layer in a climate
  * theory: monotonicity and coercivity
  * theory: Lax-Milgram --> Stampacchia
4. Finite element solutions
  * basic FE
  * the Ciarlet non-admissible picture
  * active-set methods
  * theory: Falk a priori

## lecture 2: New solver approaches for variational inequalities

TODO: Mine talks from mcd-extended/, and VI-AMR/presentations/.  Feature Falk, my extension of Falk, PDAS, HIK, Benson&Munson, Papadapoulos&Hintermuller peeling theorem, FASCD, NSV03, VIAMR.  Mention LVPP (but others have talked about that).

1.
* active-set Newton methods
* vinewtonrsls in Petsc (BM06)
* Papa. & Hintermuller: one layer of triangles per iteration
2.
* a posterior estimators, esp NSV 03
* AMR
3.
* grid sequencing
* Newton-multigrid
* FASCD
4.
* Berstein polynomials
* LVPP

## lecture 3: Stokes glacier models with Firedrake: A tutorial

slides from stokes-ice-tutorial/

## lecture 4: The mathematical (and numerical) problem of glaciation

well-posedness etc.  Mine talks from glacier-fe-estimate/talk/UW26/
