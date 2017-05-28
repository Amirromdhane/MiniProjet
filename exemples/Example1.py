#!/usr/bin/env python

import matplotlib.pyplot as plt

import networkx as nx

# Load the graph as a directed graph from a text file
G=nx.read_edgelist("graphe1.edgelist",nodetype=int,create_using=nx.DiGraph())
pos = nx.spring_layout(G)   # positions for all nodes


# nodes
nx.draw_networkx_nodes(G,pos,
                       nodelist=G.nodes(),
                       node_color='r',
                       node_size=600,
               alpha=0.8)


# edges
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
nx.draw_networkx_edges(G,pos,
                       edgelist=G.edges(),
                       width=8,alpha=0.5,edge_color='k')


# labels
labels = {}    
for node in G.nodes():
    labels[node] = str(node)

nx.draw_networkx_labels(G,pos,labels,font_size=16)

plt.axis('off')
plt.show() # display
