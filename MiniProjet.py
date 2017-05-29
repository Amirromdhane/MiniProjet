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
    node_position = nx.spring_layout(Graphe,k=1,iterations=100)     
    
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
    
    # weights
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in Graphe.edges(data=True)])
    nx.draw_networkx_edge_labels(Graphe,node_position,edge_labels=edge_labels)

    # display
    plt.axis('off') #on cache la grille de coordonnées
    plt.show() #commande d'affichage
    
def ajouterProcessus(processus):
    Graphe.add_node(processus)
    
    
def demanderRessource(processus, ressource):
    if estBloque(processus):
        print("Processus bloqué vous pouvez pas demander des ressources")
    else:
        # On calcule le poids de l'arc à créer entre le processus et la ressource
        Poids = len(Graphe.predecessors(ressource))     
        # Si le poids > 0 celà veut dire que le processus est bloqué par un ou plusieurs autres processus
        if Poids>0 :
            for i in Graphe.predecessors(ressource) :
                # On ajoute donc des arcs entre ces processus de poids -1 pour les différencier plus facilement
                Graphe.add_edge(processus, i, weight=-1)
        # On fini par ajouter notre arc entre le processus et la ressource        
        Graphe.add_edge(processus, ressource, weight=Poids)
    
def libererRessource(processus, ressource):
    if estBloque(processus):
        print("Processus bloqué vous pouvez pas libérer des ressources")
    else:
        if Graphe.number_of_edges(processus,ressource)==0 :
            print("Le processus ",processus," n'utilise pas la ressource ",ressource)
        else:
            for i in Graphe.predecessors(ressource):
                if Graphe[i][ressource]['weight'] > Graphe[processus][ressource]['weight']:
                    Graphe[i][ressource]['weight']-=1
            Graphe.remove_edge(processus,ressource)
                  
def estBloque(processus):
   for i in Graphe.successors(processus):
       if Graphe[processus][i]['weight']>0:
           return True
   return False

def detruirePrcessus(processus):
    for i in Graphe.successors(processus):
        if Graphe[processus][i]['weight']>=0:
            for j in Graphe.predecessors(i):
                if Graphe[j][i]['weight'] > Graphe[processus][i]['weight']:
                    Graphe[j][i]['weight']-=1
        Graphe.remove_edge(processus,i)
        
         
def listeAttente(ressources):
    return Graphe.predecessors(ressources)
            
def listeProcessus():
    resultat=Graphe.nodes()
    resultat=[x for x in resultat if x not in Ressources]
    return resultat

def listeActif():
    resultat=listeProcessus()
    resultat=[x for x in resultat if estBloque(x)==False]
    return resultat

# MAIN

ajouterProcessus('P1')
ajouterProcessus('P2')
ajouterProcessus('P3')
demanderRessource('P1', 'R1')
demanderRessource('P2', 'R1')
demanderRessource('P3', 'R1')
"""
if estBloque('P2'):
    print ("P2 bloqué")
else:
    print("P2 non bloqué")
if estBloque('P1'):
    print ("P1 bloqué")
else:
    print("P1 non bloqué")
libererRessource('P1', 'R1')
libererRessource('P2', 'R1')
"""
libererRessource('P1', 'R1')
print(listeAttente('R1'))
print(listeActif())
afficherGraphe()




