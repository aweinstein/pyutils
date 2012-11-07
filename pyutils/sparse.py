'''Utility functions useful when working with sparse signal models.'''

import numpy as np
from numpy.linalg import norm, pinv

def make_A(m, n, normalize=False):
    """Create `m`-by-`n` matrix with entries iid gaussian.

    If `normalize` is True, make the norm of all the columns of A equal to 1.
    """
    A = np.random.randn(m, n)
    if normalize:
        A /= np.apply_along_axis(np.linalg.norm, 0, A)
    return A

def make_sparse_x(n, k):
    """Make a vector of length `n` and sparsity `k`.

    The location of the `k` entries are chosen uniformly at random. The
    amplitude of the nonzero entries are iid drawn from a uniform distribution
    in the interval [-2, -1] U [1,2].
    """
    x = np.zeros((n, 1))
    i = np.arange(0, n)
    np.random.shuffle(i)
    supp = i[:k]
    x[supp] = np.sign(np.random.randn(k, 1)) * (np.random.rand(k, 1) + 1)
    return x

def make_group_sparse_x(n, k, J):
    """Make a group sparse vector.

    `x` is a group sparse vector of length `n` with `k`  groups of length `J`.

    The location of the `k` groups are chosen uniformly at random. The
    amplitude of the nonzero entries are iid drawn from a uniform distribution
    in the interval [-2, -1] U [1, 2].
    """
    x = np.zeros((n, 1))
    i = np.arange(0, n-1, J)
    np.random.shuffle(i)
    supp = i[:k]
    for j in range(J):
        x[supp + j] = (np.sign(np.random.randn(k, 1)) *
                       (np.random.rand(k, 1) + 1))
    return x

def omp(A, y, epsilon=1e-3):
    """Recover a sparse vector from linear observations using OMP.

    Given `y = Ax` recover `x` using a naive implementation of OMP.
    
    Parameter
    ---------
    A : array, shape = (m, n)
        Matrix representing the linear operator
    y : array, shape = (m, 1)
        Linear observations
    epsilon : float, optional
        Stoping condintion is ||residue|| < epsilon

    Return
    ------
    x_hat : array, shape = (n, 1)
        Estimate of x

    Note: This is a naive inefficient implementation of OMP. For an efficient
    implementation see the scikit-learn implementation (http://bit.ly/Re4NJt)
    """
    n = A.shape[1]
    r = y.copy()
    k = 1
    Delta = []
    while norm(r) > epsilon:
        h = np.abs(np.dot(A.T, r))
        Delta.append(np.argmax(h))
        alpha = np.linalg.lstsq(A[:,Delta], y)[0]
        r = y - np.dot(A[:, Delta], alpha)
        k += 1

    x_hat = np.zeros((n, 1))
    x_hat[Delta] = alpha

    return x_hat

def bomp(A, y, J, epsilon=1e-3):
    """Recover a sparse vector from linear observations using BOMP.

    Given `y = Ax` recover `x` using a naive implementation of BOMP.
    
    Parameter
    ---------
    A : array, shape = (m, n)
        Matrix representing the linear operator
    y : array, shape = (m, 1)
        Linear observations
    J : integer
        Length of each group
    epsilon : float, optional
        Stoping condintion is ||residue|| < epsilon

    Return
    ------
    x_hat : array, shape = (n, 1)
        Estimate of x

    Note: This is a naive inefficient implementation of OMP. For an efficient
    implementation see the scikit-learn implementation (http://bit.ly/Re4NJt)
    """
    n = A.shape[1]
    r = y.copy()
    k = 1
    I = [] # Group indices
    Iv = np.zeros(n, 'bool') # Vector indices
    nJ = n / J # Number of groups
    _gs = lambda j,J=J: slice(j*J,(j+1)*J)

    while norm(r) > epsilon:
        h = np.zeros(nJ)
        for j in range(nJ):
             h[j] = norm(np.dot(A[:,_gs(j)].T, r))
        i_star = np.argmax(h)
        I.append(i_star)
        Iv[_gs(i_star)] = True
        alpha = np.linalg.lstsq(A[:,Iv], y)[0]
        r = y - np.dot(A[:, Iv], alpha)

    x_hat = np.zeros((n, 1))
    x_hat[Iv] = alpha

    return x_hat

    
