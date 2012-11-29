import numpy as np


def array_to_tex(a, fmt=None):
    """Latex representation of a NumPy array. 

    If `fmt` is not `None` use it to format each entry of `a`, otherwise use
    `str`.
    
    Based on http://bit.ly/Qrr9t4
    """
    if fmt is not None:
        f = lambda x, fmt=fmt: fmt % x
    else:
        f = str
    s = ' \\\\\n'.join([' & '.join(map(f, line)) for line in a])
    s += ' \\\\'
    return s
