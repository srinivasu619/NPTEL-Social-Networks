import networkx as nx
import itertools as it
import matplotlib.pyplot as plt

def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()
    e = G.number_of_edges()

    first_community = []
    for i in range(1,n//2+1):
        for j in it.combinations(nodes,i):
            first_community.append(list(j))
    
    second_community = []
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)
    
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = []

    for i in range(len(first_community)):
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())

    for i in range(len(second_community)):
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())

    # print(first_community)
    # print(second_community)
    # print(num_intra_edges1)
    # print(num_intra_edges2)
    for i in range(len(first_community)):
        num_inter_edges.append(e-num_intra_edges1[i]-num_intra_edges2[i])

    # print(num_inter_edges)

    for i in range(len(first_community)):
        ratio.append((float)((num_intra_edges1[i]+num_intra_edges2[i])/num_inter_edges[i]))

    maxIndex = ratio.index(max(ratio))
    print(first_community[maxIndex])
    print(second_community[maxIndex])
G = nx.barbell_graph(3,0)
# nx.draw(G)
# plt.show()
communities_brute(G)