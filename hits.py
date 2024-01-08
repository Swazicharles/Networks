import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np


A=[[0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0]]

C = [[0, 3, 0, 5, 2, 0], 
    [3, 0, 5, 0, 2, 0], 
    [0, 5, 0, 3, 0, 2], 
    [5, 0, 3, 0, 0, 2], 
    [2, 2, 0, 0, 0, 2], 
    [0, 0, 2, 2, 2, 0]]

S = nx.DiGraph(np.array(A))

P = nx.DiGraph(np.array(C))

T = nx.minimum_spanning_tree(P)
print(T)

hubs, authorities = nx.hits(S, max_iter = 50, normalized = True)
# The in-built hits function returns two dictionaries keyed by nodes
# containing hub scores and authority scores respectively.
 
print("Hub Scores: ", hubs)
print("Authority Scores: ", authorities)