import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

A=[[1,1,1,1],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]]


S = nx.DiGraph(np.array(A))

nx.draw(S, with_labels=True)
plt.show()

centrality = nx.eigenvector_centrality(S, tol =0.01)
for n, c in centrality.items():
    print(n, f"{c : f}")