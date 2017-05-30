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
    node_position = nx.spring_layout(Graphe,k=2,iterations=100)     
    
    # nodes
    nx.draw_networkx_nodes(Graphe,node_position,
                       nodelist=Graphe.nodes(),
                       node_color='red',
                       node_size=1500,
                       alpha=1.0)
    
    nx.draw_networkx_nodes(Graphe,node_position,
                       nodelist=Ressources,
                       node_color='green',
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
    
def ajouterProcessus():
    processus=input("Entrez le nom du processus : ")
    Graphe.add_node(processus)
    
     
        
def corrigerPoids(proc1, proc2) :
    for i in Ressources :
        if proc1 in Graphe.predecessors(i) and proc2 in Graphe.predecessors(i):
            Graphe[proc1][proc2]['weight']-=1  
    
def attribuerRessource(processus, ressource) :
    # On calcule le poids de l'arc à créer entre le processus et la ressource
    Poids = len(Graphe.predecessors(ressource))  
    # On ajoute notre arc entre le processus et la ressource 
    Graphe.add_edge(processus, ressource, weight=Poids)
    # Si le poids > 0 celà veut dire que le processus est bloqué par un ou plusieurs autres processus
    if Poids>0 :
        for i in Graphe.predecessors(ressource) :
            if i!=processus :
                # On ajoute donc des arcs entre ces processus de poids -1 par défaut
                Graphe.add_edge(processus, i, weight=0)
                # On corrige le poids de l'arc entre les processus bloquants et le processus actuel (-D avec D le degré de blocage)
                corrigerPoids(processus, i)
        
    
def demanderRessource():
    processus=input("Entrez le nom du processus : ")
    if not Graphe.has_node(processus):
        Graphe.add_node(processus)
    ListeRessource=input("Entrez la liste des nom des ressources : ").split()
    if estBloque(processus):
        print("Processus bloqué vous pouvez pas demander des ressources")
    else:
        for i in ListeRessource :
            attribuerRessource(processus, i)
               
        
        
        
def libererRessource():
    processus=input("Entrez le nom du processus : ")
    ressource=input("Entrez le nom du ressource : ")
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
            for j in Graphe.predecessors(ressource):
                if Graphe[j][processus]['weight']==-1:
                    Graphe.remove_edge(j,processus)
                else:
                    Graphe[j][processus]['weight']+=1
                      
                  
def estBloque(processus):
   for i in Graphe.successors(processus):
       if Graphe[processus][i]['weight']>0:
           return True
   return False

def detruirePrcessus():
    processus=input("Entrez le nom du processus : ")
    if processus  in Ressources:
        print("On peut pas detruire des Ressources")
    else:
        for i in Graphe.successors(processus):
            if Graphe[processus][i]['weight']>=0:
                for j in Graphe.predecessors(i):
                    if Graphe[j][i]['weight'] > Graphe[processus][i]['weight']:
                        Graphe[j][i]['weight']-=1
            Graphe.remove_edge(processus,i)
        Graphe.remove_node(processus)
        
         
def listeAttente():
    ressource=input("Entrez le nom du ressource : ")
    if len(Graphe.predecessors(ressource))==0:
        print("Liste d'attente vide pour ",ressource)
    else:
        print("Liste attente pour ",ressource," est la suivante :",Graphe.predecessors(ressource))
    return Graphe.predecessors(ressource)
            
def listeProcessus():
    resultat=Graphe.nodes()
    resultat=[x for x in resultat if x not in Ressources]
    return resultat

def listeActif():
    resultat=listeProcessus()
    resultat=[x for x in resultat if estBloque(x)==False]
    print("Les processus actifs sont les suivant : ",resultat)
    return resultat

def bloqueurs():
    none=0
    for i in listeProcessus():
        resultat=[x for x in listeProcessus() if Graphe.has_edge(i,x)]
        if len(resultat)!=0:
            print("Le processus ",i," est bloqué par les processus suivants : ",resultat)
            none+=1
    if none==0:
        print("Aucun processus n'est bloqué")

def processus_interblocage():
    if len(detect_interblocage())==0:
        print("Il y'a pas d'interblocage")
    else:
        print("Les processus concerné par un interblocage sont les suivants :",detect_interblocage())


def detect_interblocage():
    resultat=[]
    for i in listeProcessus():
        for j in listeProcessus():
            if nx.has_path(Graphe,i,j) and nx.has_path(Graphe,j,i) and j!=i:
                resultat.extend([i,j])
    return resultat



# MAIN

choix=-1
fichier1=open("data1.txt","rt").read()
fichier2=open("data2.txt","rt").read()

while choix !='0' :
    if len(detect_interblocage())==0 :
        print (fichier1)
        choix=input("Choissisez une commande : ")
        options = {'0' : exit,
                   '1' : ajouterProcessus,
                   '2' : detruirePrcessus,
                   '3' : demanderRessource,
                   '4' : libererRessource,
                   '5' : listeAttente,
                   '6' : listeActif,
                   '7' : bloqueurs,
                   '8' : processus_interblocage,
                   '9' : afficherGraphe,
                  }
        options[choix]()
    else:
        print (fichier2)
        choix=input("Choissisez une commande : ")
        options = {'0' : exit,
                   '1' : detruirePrcessus,
                   '2' : listeAttente,
                   '3' : listeActif,
                   '4' : bloqueurs,
                   '5' : processus_interblocage,
                   '6' : afficherGraphe,
                  }
        options[choix]()


    
