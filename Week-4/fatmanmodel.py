import networkx as nx
import matplotlib.pyplot as plt
import random

# adding Hundred nodes to create a network
def create_network():
    G=nx.Graph()
    G.add_nodes_from(range(1,101))
    return G

#added Random BMI for the network Nodes
def assign_random_BMI(G):
    for node in G.nodes():
        G.node[node]['name'] = random.randint(15,40)
        G.node[node]['type'] = 'person'

#extracting labels for the nodes
def extract_labels(G):
    labeldict={}
    for node in G.nodes():
        labeldict[node] =  G.node[node]['name']
    return labeldict

#extracting the size of the nodes
def extract_size(G):
    arr_size = []
    for node in G.nodes():
        arr_size.append(G.node[node]['name']*20)
    return arr_size
#plotting the graph
def plot_graph(G,labeldict,size):
    nx.draw(G,labels=labeldict ,node_size=size)
    plt.show()        


G = create_network()
assign_random_BMI(G)
dict_label = extract_labels(G)
arr_size = extract_size(G)
plot_graph(G,dict_label,arr_size)
