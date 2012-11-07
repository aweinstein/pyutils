import numpy as np
import matplotlib.pyplot as plt
from pyutils.sparse import bomp, omp, make_A, make_group_sparse_x

def rate_of_recovery():
    print 'Computing rate of recovery of BOMP and OMP'
    n = 256
    m = 64
    J = 3
    trials = 100
    ks = range(1, 16)
    succs_omp, succs_bomp = [], []
    for k in ks:
        succ_omp, succ_bomp = 0, 0
        print 'Running trials for k = %d' % k
        for _ in range(trials):
            x = make_group_sparse_x(n, k, J)
            A = make_A(m, n, normalize=True)
            y = np.dot(A, x)
            x_hat_omp = omp(A, y)
            x_hat_bomp = bomp(A, y, J)
            error_omp = np.linalg.norm(x - x_hat_omp)
            error_bomp = np.linalg.norm(x - x_hat_bomp)
            if error_omp < 1e-3:
                succ_omp += 1
            if error_bomp < 1e-3:
                succ_bomp += 1
        succs_omp.append(float(succ_omp) / trials)
        succs_bomp.append(float(succ_bomp) / trials)

    plt.figure()
    plt.plot(ks, succs_omp, label='omp')
    plt.plot(ks, succs_bomp, label='bomp')
    plt.legend()
    plt.xlabel('group sparsity k')
    plt.ylabel('rate of recovery')
    plt.title('Rate of recovery usigin OMP\n n = %d m = %d J = %d' % (n, m, J))
    plt.ylim(-0.1, 1.1)
    plt.show()

if __name__ == '__main__':
    rate_of_recovery()

## print 'Testing OMP'
## n = 256
## m = 64
## k = 4
## J = 3
## x = make_group_sparse_x(n, k, J)
## A = make_A(m, n, normalize=True)
## y = np.dot(A, x)
## x_hat_omp = omp(A, y)
## x_hat_bomp = bomp(A, y, J)
## error_omp = np.linalg.norm(x - x_hat_omp)
## error_bomp = np.linalg.norm(x - x_hat_bomp)

## print 'OMP error: %.2f' % error_omp
## print 'BOMP error: %.2f' % error_bomp
