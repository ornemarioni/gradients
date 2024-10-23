# Es el mismo que el programa que David pero hecho a mi gusto
import numpy as np


def rbin1(x, nbin):

    x_sort = np.sort(x)

    n = len(x)

#     print(n)
    if np.mod(n, nbin) == 0:
        delta = int(n / nbin) - 1
    else:
        delta = int(n / nbin)

#     print(delta)

    med = np.zeros(nbin)

    nodos = np.zeros(nbin+1)
    nodos[0] = x_sort[0]

    for i in range(0, nbin):
        med[i] = np.median(x_sort[i*delta:(i+1)*delta])
        # med[i] = np.mean(x_sort[i*delta:(i+1)*delta])
        nodos[i+1] = x_sort[(i+1)*delta]

    return med, nodos


# aca se agregaron los nodos,tengo que modificar los programas que usan esto
