import networkx as nx

def plot_grid(G):
    '''Plot G in a grid.

    The nodes of G are assumed to be of the form (i,j). The (i,j) value is used
    to locate each node.
    '''
    pos = dict(((i,j),(j,-i)) for i,j in G.nodes())
    nx.draw(G, pos=pos, node_size=400, font_size=8, alpha=0.8)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    G = nx.grid_2d_graph(5,8)
    plot_grid(G)
    plt.show()
