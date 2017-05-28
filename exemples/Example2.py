#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

def fermeture(G):
    
    for k in G.nodes():
        for i in G.nodes():
            for j in G.nodes() :     
                if i in G.predecessors(k) and j in G.successors(k):
                    
                    G.add_edge(i,j,weight=k)
                    
                
    
    
# Load data from a formatted file
df = pd.read_csv('data.txt', sep=' ')

# a new empty graph object
G2 = nx.DiGraph()

# create nodes with properties from dataframe (two examples shown, but any number
# of properties can be entered into the attributes dictionary of each node)
for idx, row in df.iterrows():
    G2.add_edge(int(row['Source']), int(row['Destination']), weight=int(row['Weight']))
fermeture(G2)
pos=nx.spring_layout(G2) 

# construct a list of colors from the nodes so we can render with that property
nx.draw_networkx(G2,pos)
edge_labels=dict([((u,v,),d['weight']) for u,v,d in G2.edges(data=True)])
nx.draw_networkx_edge_labels(G2,pos,edge_labels=edge_labels)
plt.show() # display



    