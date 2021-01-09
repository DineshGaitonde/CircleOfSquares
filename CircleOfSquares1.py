# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:20:12 2021

"""

import math
import networkx as nx
import itertools

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

def hamilton(G):
    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1])
                     if node != path[-1]) #exclude self loops
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n and G.has_edge(p[0], p[-1]):
                return p
            else:
                F.append((g,p))
    return None

maxNum = 40
numbers = [idx+1 for idx in range(maxNum)]
squaredFriends = {a:[] for a in numbers}


for a, b in itertools.product(numbers, numbers):
    if is_square(a+b):
        squaredFriends[a].append(b)
        squaredFriends[b].append(a)


G = nx.Graph()
for a, bList in squaredFriends.items():
    for b in bList:
        if a < b:
            G.add_edge(a, b)
           

print(hamilton(G))
