from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt

def plot_grid(G):
    '''Plot G in a grid.

    The nodes of G are assumed to be of the form (i,j). The (i,j) value is used
    to locate each node.
    '''
    pos = dict(((i,j),(j,-i)) for i,j in G.nodes())
    nz = min(2000.0 / sqrt(len(G)), 400)
    nx.draw(G, pos=pos, node_size=nz, font_size=0, alpha=0.8)
    plt.axis('equal')
    
def random_walk(G, nodelist=None):
    '''Return the random walk matrix associated with the graph.

    The random walk matrix is defined as P = D^-1 * W, where D and W are the
    degree and adjancency matrix, respectively.

    Parameters
    ----------
    G : networkx graph

    nodelist: list, optional
       The rows and columns are ordered according to the nodes in nodelist. If
       nodelist is None, then the ordering is produced by G.nodes().

    Returns
    -------
    P : NumPy matrix
       Random walk matrix of G
    '''
    W = nx.to_numpy_matrix(G, nodelist=nodelist)
    D = W.sum(1)
    P = W / D

    return P

if __name__ == '__main__x':
    G = nx.cycle_graph(5)
    P = random_walk(G)
    print P
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    N = 10
    G = nx.grid_2d_graph(N, N)
    plot_grid(G)
    plt.show()
