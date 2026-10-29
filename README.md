# icl26

I am giving a series of 4 applied/computational mathematical lectures at Imperial College London, in October and November of 2026.

This repository contains the slides and source materials for lectures 1 and 2.  Links to PDFs and sources for lectures 3 and 4 are also below.  The slides themselves, and the demonstration codes they mention, are all open source, and the repository has a generous MIT license.  Please re-use as much LaTeX, Tikz, and Python as you wish, but please give me credit as you go.

## abstract for the series

The lecture series introduces variational inequalities (VIs) to a general applied mathematical audience, pursues their finite element solution, and applies them to a geophysical problem.  VIs are partial differential equation weak forms, but subject to bounds (inequality constraints) on their solution(s).  They reformulate how one might pose boundary conditions at a free location; where the conditions apply is now determined simultaneously with the solution.  Certain VIs state the KKT conditions of optimization problems in function spaces, but in all cases these continuum models introduce admissibility and complementarity concerns into numerical solver methodology.  Examples of VIs include the classical obstacle problem, the problem of elastic contact, and, as I will emphasize, the problem of finding the extent of glaciation in a time- and space-varying climate.  Recent results and open problems will appear, regarding multigrid approaches, adaptive mesh refinement, higher-order elements, and well-posedness of the glacier model.

## lecture 1 on 20 October: Introduction to variational inequalities and their finite element solution

See [slides-oct20.pdf](slides-oct20.pdf), with LaTeX sources in [talk1/](talk1/).

## lecture 2 on 27 October: A survey of new solvers for variational inequalities

See [slides-oct27.pdf](slides-oct27.pdf), with LaTeX sources in [talk2/](talk1/).

## lecture 3 on 3 November: Stokes glacier models with Firedrake: A tutorial

This lecture uses the existing slides from [stokes-ice-tutorial/](https://github.com/bueler/stokes-ice-tutorial).

## lecture 4 on 17 November: The mathematical (and numerical) problem of glaciation

TODO: well-posedness and extruded-mesh solvers.  Mine talks from glacier-fe-estimate/talk/UW26/
