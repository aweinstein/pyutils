import bisect
import random
import sys
import functools

# From http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
# note that this decorator ignores **kwargs
def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

def progress(msg):
    sys.stdout.write('\r' + msg)
    sys.stdout.flush()

def choose(a, p):
    """Choose randomly an item from `a` with pmf given by p.

    a : list
    p : probability mass function
    """
    # TODO: Raise an exception if len(a) != len(p) or if sum(p)~= 1
    intervals = [sum(p[:i]) for i in range(len(p))]
    item = a[bisect.bisect(intervals, random.random()) - 1]
    return item

def factors(value):
    """List all the factors of an integer.

    Source:
    http://stackoverflow.com/a/5505024/349087
    """
    if value < 1:
        return []
    factors = [(1, value)]
    for i in range(2, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, value / i))
    return factors

def call(argv, locals):
    """Call function contained in argv.

    argv : list with the command line arguments, typically sys.argv
    locals : dictionary with module variables

    This function try to call named `argv[1]`, such that executing

    $ python foo.py f1

    will, if it exists, function `f1` defined in foo.py.
    """

    if len(sys.argv) >= 2:
        fname = sys.argv[1]
        if locals.has_key(fname) and hasattr(locals[fname], '__call__'):
            locals[fname]()
        else:
            print 'Function %s does not exist' % fname
    else:
        print 'Wrong number of arguments.'

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
        print 'p: %.3f freq: %.2f' % (prob, float(h[e])/n)

def test_progress():
    import time
    for i in range(100):
        progress('Progress: %d%%' % i)
        time.sleep(0.2)

if __name__ == '__main__':
    test_choose()
