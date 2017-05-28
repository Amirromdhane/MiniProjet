import networkx as nx
G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])

H=nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

T=nx.Graph()
T.add_edge(1,2)
e=(2,3)
T.add_edge(*e) 

D=nx.Graph()
D.add_edges_from([(1,2),(1,3)])
D.add_edges_from(H.edges())

#Graph.remove_node()
#Graph.remove_nodes_from()
#Graph.remove_edge()
#Graph.remove_edges_from()

G.remove_node(H)

D.clear()

F=nx.Graph()
F.add_edges_from([(1,2),(1,3)])
F.add_node(1)
F.add_edge(1,2)
F.add_node("spam")       # adds node "spam"
F.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'

print(list(G.nodes()))
print(list(H.nodes()))
print(list(T.nodes()))
print(list(D.nodes()))
print(list(F.nodes()))

#http://networkx.readthedocs.io/en/networkx-1.11/tutorial/tutorial.html