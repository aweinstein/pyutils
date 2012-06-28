import networkx as nx

def plot_grid(G):
    '''Plot G in a grid.

    The nodes of G are assumed to be of the form (i,j). The (i,j) value is used
    to locate each node.
    '''
    #TODO: Set the dimensions according to the size of the graph
    pos = dict(((i,j),(j,-i)) for i,j in G.nodes())
    nx.draw(G, pos=pos, node_size=400, font_size=8, alpha=0.8)

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
    G = nx.grid_2d_graph(5,8)
    plot_grid(G)
    plt.show()
