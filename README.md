# icl26

I plan to give four applied mathematical lectures at Imperial College London, in October and November of 2026.  This README is my planning document, and this repository contains the slides for lectures 1 and 2.  Links to PDFs and sources for lectures 3 and 4 are also given below.  The slides themselves, and the demonstration codes they mention, are all open source; scrape as much LaTeX, Tikz, and Python as you want!

## common abstract for the series

This four-lecture series introduces variational inequalities to a general applied mathematical audience, pursues their finite element solution, and applies them to a geophysical problem.  Variational inequalities are partial differential equation weak forms, but subject to bounds on their solution(s).  They reformulate how one might pose boundary conditions at a free location; where the conditions apply is now determined simultaneously along with the solution.  Certain variational inequalities state the KKT conditions of optimization problems in function spaces, and in all cases these continuum models introduce admissibility and complementarity concerns into numerical solver methodology.  Examples of variational inequalities include the classical obstacle problem, the problem of elastic contact, and, as I will emphasize, the problem of finding the extent of glaciation in a time- and space-varying climate.  Recent results and open problems will appear, regarding multigrid approaches, adaptive mesh refinement, higher-order elements, and well-posedness of the glacier model.

## lecture 1: introduction to VI models and their FE solutions

TODO: Mine talks-public/2014/DMScolloq/ talk.  (Its pdf is at https://www.pism.io/uaf-iceflow/buelerDMScolloqJan2014.pdf)  Examples/intro includes starting with examples: calc 1 example, distance to a closed convex set example, convex minimization, classical obstacle problem, fluid layer problem, Signorini.  Theory: Lax-Milgram for K, monotone ops.  FE setup, Falk a priori.

## lecture 2: modern solvers and meshers for VIs

TODO: Mine talks from mcd-extended/, and VI-AMR/presentations/.  Feature Falk, my extension of Falk, PDAS, HIK, Benson&Munson, Papadapoulos&Hintermuller peeling theorem, FASCD, NSV03, VIAMR.  Mention LVPP (but others have talked about that).

## lecture 3: Firedrake for the Stokes glacier problem

slides from stokes-ice-tutorial/

## lecture 4: the main thread in mathematical glaciology

well-posedness etc.  Mine talks from glacier-fe-estimate/talk/UW26/
