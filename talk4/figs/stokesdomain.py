#!/usr/bin/env python3

# generates notation{1|2|3}.pdf (overlays)
# Stokes domain over Omega, with bed z=b(x) and climate a(t,x)
# second adds thickness H and the label Lambda(t)
# labels are typeset by lualatex in Fira Sans/Fira Math to match the slides
# adapted from glacier-fe-estimate/talk/UW26/figs/stokesdomainusual.py

import numpy as np
import matplotlib
matplotlib.use("pgf")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "lualatex",
    "pgf.rcfonts": False,
    "font.family": "sans-serif",
    "pgf.preamble": "\n".join([
        r"\usepackage{unicode-math}",
        r"\setsansfont{Fira Sans Book}",
        r"\setmainfont{Fira Sans Book}",
        r"\setmathfont{Fira Math}",
    ]),
})

bigfsize = 24.0

def genbasicfig(xshift=0.0, icefrees=True):
    x = np.linspace(0.0,10.0,1001)
    # bed elevation
    b = 0.07*(x-3.0)**2 + 0.2*np.sin(2.0*x) - 0.1
    plt.plot(x + xshift, b, 'k--', lw=2.5)
    # current thickness
    h0 = 3.0
    L = 3.0
    firstshape = h0*(-0.2 + np.sqrt(np.maximum(0.0,1.0 - (x-5)**2/L**2)))
    thk = np.maximum(0.0, firstshape)
    # surface
    xx = x + xshift
    s = b + thk
    offset = 0.0  # ice-free surface lies exactly on the bed
    if icefrees:
        plt.plot(xx, s + offset, 'k', lw=3.0)
    else:
        plt.plot(xx[thk > 0], s[thk > 0] + 0.1 * offset, 'k', lw=3.0)
    return xx, s, b

def drawclimate(x,s):
    plt.text(x[10], s[10]+2.7, r'$a(t,x)$', fontsize=bigfsize, color='k')
    for j in range(10):
        xarr = x[50+100*j]
        if j>0:
            magarr = 0.6*np.sin(np.pi/2 + 0.6*xarr)
        else:
            magarr = 0.05
        plt.arrow(xarr, s.max()+0.3, 0.0, magarr,
                  lw=1.5, head_width=0.1, color='k')

greycolor = '0.5'

def notationfig(filename, number):
    # both figures draw everything, so bounding boxes agree for overlays;
    # in the first figure the H arrow and Lambda label are fully transparent
    plt.figure(figsize=(10,4.6))
    x, s, b = genbasicfig()
    if number == 1:
        plt.text(x[480], b[600] + 0.4 * s[600], 'ice',
                 fontsize=bigfsize, color='k')
    if number == 2:
        plt.text(x[550] + 0.1, b[600] + 0.4 * s[600], r'$\Lambda(t)$',
                 fontsize=bigfsize, color='k')
    if number == 3:
        plt.text(x[480], b[600] + 0.4 * s[600], r'$\Lambda(t)$',
                 fontsize=bigfsize, color='k')
    if number == 2:
        jH = 350  # thickness arrow location
        plt.annotate('', xy=(x[jH], s[jH]), xytext=(x[jH], b[jH]),
                    arrowprops=dict(arrowstyle='<->', color=greycolor, lw=2.0,
                                    shrinkA=0, shrinkB=0))
        plt.text(x[jH] + 0.1, 0.5 * (b[jH] + s[jH]) - 0.15, r'$H(t,x)$',
                fontsize=bigfsize, color=greycolor)
    drawclimate(x,s)
    if number >= 2:
        plt.text(x[150], s[300] + 0.7, r'$z=s(t,x)$', fontsize=bigfsize, color='k')
    plt.text(x[650], b[650] - 0.5, r'$z=b(x)$', fontsize=bigfsize, color='k')
    yR = min(b) - 0.5
    plt.plot([min(x),max(x)],[yR,yR],color='k',lw=1.0,clip_on=False)  # bottom of Omega
    plt.text(x[875], yR+0.2, r'$\Omega$', fontsize=bigfsize, color='k')
    if number == 2:
        # glaciated region Lambda(t)^perp, as thicker grey segment along Omega
        glac = (s - b > 0.0)
        xg = x[glac]
        plt.plot([xg.min(), xg.max()], [yR+0.03, yR+0.03], color=greycolor, lw=5.0,
                solid_capstyle='butt', clip_on=False)
        plt.text(0.5 * (xg.min() + xg.max()) + 0.5, yR + 0.25, r'$\Lambda(t)^\perp$',
                fontsize=bigfsize, color=greycolor)
    if number == 3:
        plt.text(x[740], s[740] + 0.1, r'$\Gamma_s(t)$', fontsize=bigfsize, color=greycolor)
        plt.text(x[400], b[400] - 0.5, r'$\Gamma_b(t)$', fontsize=bigfsize, color=greycolor)
    plt.axis([0.0,10.0,yR,4.5])
    plt.axis('off')
    print('writing file %s' % filename)
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.0, transparent=True)
    plt.close()

notationfig('notation1.pdf', 1)
notationfig('notation2.pdf', 2)
notationfig('notation3.pdf', 3)
