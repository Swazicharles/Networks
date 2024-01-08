import networkx as nx
import numpy as np


# create graph from adjacency matrix
A = [[0, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

B= [[0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0]]

G = nx.DiGraph(np.array(B))

# compute Katz centrality with default parameters
centrality = nx.katz_centrality(G, alpha=0.1, beta=1)

Q = nx.DiGraph(np.array(B))
pr =  nx.pagerank(Q, alpha=0.85)

for node, value in pr.items():
    print(f"Node {node}: pagerank Centrality = {value:f}")




# normalize the centrality vector
norm_factor = sum(v**2 for v in centrality.values())**0.5
centrality = {k: v/norm_factor for k, v in centrality.items()}

# print results
#print(f"Node 0: {centrality[0]:f}")
#print(f"Node 1: {centrality[1]:f}")
#print(f"Node 2: {centrality[2]:f}")
#print(f"Node 3: {centrality[3]:f}")
#print(f"Node 4: {centrality[4]:f}")
#print(f"Node 5: {centrality[5]:f}")
#print(f"Node 6: {centrality[6]:f}")



