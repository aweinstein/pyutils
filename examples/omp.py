import numpy as np
import matplotlib.pyplot as plt
from pyutils.sparse import omp, make_A, make_sparse_x

def rate_of_recovery():
    print 'Computing rate of recovery of OMP'
    n = 256
    m = 64

    trials = 200
    ks = range(2, 21, 2)
    succs = []
    for k in ks:
        succ = 0
        print 'Running trials for k = %d' % k
        for _ in range(trials):
            x = make_sparse_x(n, k)
            A = make_A(m, n, normalize=True)
            y = np.dot(A, x)
            x_hat = omp(A, y)
            error = np.linalg.norm(x - x_hat)
            if error < 1e-3:
                succ += 1
        succs.append(float(succ) / trials)

    plt.figure()
    plt.plot(ks, succs)
    plt.xlabel('sparsity k')
    plt.ylabel('rate of recovery')
    plt.title('Rate of recovery usigin OMP\n n = %d m = %d' % (n, m))
    plt.ylim(-0.1, 1.1)
    plt.show()

def speed_test():
    import timeit

    setup = '''\
import numpy as np
from pyutils.sparse import omp, make_A, make_sparse_x
n = 256
m = 64
k = 20
x = make_sparse_x(n, k)
A = make_A(m, n, normalize=True)
y = np.dot(A, x)
    '''
    n = 10
    print timeit.timeit('omp(A, y)', setup=setup, number=n) / n

if __name__ == '__main__':
    speed_test()

