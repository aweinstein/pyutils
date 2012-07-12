import bisect
import random
import sys

def progress(msg):
    sys.stdout.write('\r' + msg)
    sys.stdout.flush()

def choose(a, p):
    '''Choose randomly an item from `a` with pmf given by p.

    a : list
    p : probability mass function
    '''
    # TDOO Raise an exception if len(a) != len(p) or if sum(p)~= 1
    intervals = [sum(p[:i]) for i in range(len(p))]
    item = a[bisect.bisect(intervals, random.random()) - 1]
    return item

def test_choose():
    print 'Testing choose'
    from collections import defaultdict
    n = 1000
    h = defaultdict(int)
    a = list('abcde')
    p =[0.2, 0.3, 0.1, 0.15, 0.25]
    for _ in range(n):
        h[choose(a,p)] += 1

    for prob,e in zip(p,a):
        print 'p:%f freq:%.2f' % (prob, float(h[e])/n)

def test_progress():
    import time
    for i in range(100):
        progress('Progress: %d%%' % i)
        time.sleep(0.2)

if __name__ == '__main__':
    test_choose()
