
import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np

A = [[0, 1, 0, 1, 0, 0, 0, 0], 
    [1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 1, 0, 0, 0], 
    [1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0]]


G = nx.Graph(np.array(A))

f = nx.algebraicconnectivity.fiedler_vector(G)

print(f)