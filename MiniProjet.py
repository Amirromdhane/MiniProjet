# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:35:15 2017

Object : MINI PROJECT - BASIC RESSOURCES ALLOCATOR 

@author: BOUREAU Louis
         ROMDHANE Amir
"""

import matplotlib.pyplot as plt
import networkx as nx


#Création du graphe
Graphe = nx.DiGraph()

#Initialisation des ressources 
Ressources = ['R1','R2','R3']
Graphe.add_nodes_from(Ressources)         
                    
def afficherGraphe():
    #Définition du mode d'affichage du graphe (spectral ou spring)
    node_position = nx.spring_layout(Graphe)     
    
    # nodes
    nx.draw_networkx_nodes(Graphe,node_position,
                       nodelist=Graphe.nodes(),
                       node_color='red',
                       node_size=1500,
                       alpha=1.0)
    # edges
    nx.draw_networkx_edges(Graphe,node_position,width=1.0,alpha=0.5)
    nx.draw_networkx_edges(Graphe,node_position,
                       edgelist=Graphe.edges(),
                       width=10,alpha=0.7,edge_color='black')
    # labels
    labels = {}    
    for node in Graphe.nodes():
        labels[node] = str(node)

    nx.draw_networkx_labels(Graphe,node_position,labels,font_size=18)

    # display
    plt.axis('off') #on cache la grille de coordonnées
    plt.show() #commande d'affichage
    
def ajouterProcessus(processus):
    Graphe.add_node(processus)
    
    
def demanderRessource(processus, ressource):
    Graphe.add_edge(processus, ressource, weight=0)
    
    
# MAIN

ajouterProcessus('P1')

demanderRessource('P1', 'R1')

afficherGraphe()




