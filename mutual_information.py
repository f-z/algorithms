import numpy as np


def mutual_information(arr):
    pi, pj = marginals(arr)

    h_i = shannon_entropy(pi)
    h_j = shannon_entropy(pj)
    h_ij = shannon_entropy(arr)

    mi = h_i + h_j - h_ij
    return  mi


def shannon_entropy(a):
    a = a[np.nonzero(a)]
    return -np.sum(a*np.log(a))


def marginals(a):
    marginal_sums = []
    ranged = list(range(a.ndim))
    for k in ranged:
        marginal = np.apply_over_axes(np.sum, a, [j for j in ranged if j != k])
        marginal_sums.append(marginal)
    return marginal_sums

a = np.arange(8).reshape(4,2)
