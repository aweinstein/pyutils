'''Utility functions useful when working with sparse signal models.'''

import numpy as np

def make_A(m, n, normalize=False):
    '''Create `m`-by-`n` matrix with entries iid gaussian.

    If `normalize` is True, make the norm of all the columns of A equal to 1.
    '''
    A = np.random.randn(m, n)
    if normalize:
        A /= np.apply_along_axis(np.linalg.norm, 0, A)
    return A

def make_sparse_x(n, k):
    '''Make a vector of length `n` and sparsity `k`.

    The location of the `k` entries are chosen uniformly at random. The
    amplitude of the nonzero entries are iid drawn from a uniform distribution
    in the interval [-2, -1] U [1,2].
    '''
    x = np.zeros((n, 1))
    i = np.arange(0, n)
    np.random.shuffle(i)
    supp = i[:k]
    x[supp] = np.sign(np.random.randn(k, 1)) * (np.random.rand(k, 1) + 1)
    return x

def make_group_sparse_x(n, k, J):
    '''Make a vector of length `n` and group sparsity `k`.

    The location of the `k` groups are chosen uniformly at random. The
    amplitude of the nonzero entries are iid drawn from a uniform distribution
    in the interval [-2, -1] U [1,2].
    '''
    x = np.zeros((n, 1))
    i = np.arange(0, n, J)
    np.random.shuffle(i)
    supp = i[:k]
    for j in range(J):
        x[supp + j] = (np.sign(np.random.randn(k, 1)) *
                       (np.random.rand(k, 1) + 1))
    return x
