import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np
# Import math Library
import math

C = [[0, 3, 6, 5], 
    [3, 0, 5, 6], 
    [6, 5, 0, 3], 
    [5, 3, 6, 0]]


G = nx.Graph(np.array(C))
MST = nx.minimum_spanning_tree(G)

total_weight = sum([MST[u][v] ['weight'] for u, v in MST.edges()])

print(G)
print(total_weight)



# Initialize the number of items to choose from
n = 25

# Initialize the number of possibilities to choose
k = 12

# Print total number of possible combinations
print (math.comb(n, k))
