import networkx as nx

def give_edge(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples  = sorted(dict1.items(), key=lambda x:x[1],reverse=True)
    return list_of_tuples[0][0]

def print_nodes(l):
    for i in l:
        print(i.nodes())
def seperate_communities(G):
    l = list(nx.connected_component_subgraphs(G))
    while len(l) == 1:
        l = list(nx.connected_component_subgraphs(G))
        G.remove_edge(*give_edge(G))
        print_nodes(l)

G=nx.barbell_graph(5,0)
seperate_communities(G)