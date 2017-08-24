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

#adding focii for the network
def add_focii(G):
    n = G.number_of_nodes()
    i = n+1
    focii = ['gym','movie_club','karate_club','eatout','yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G.node[i]['name'] = focii[j]
        G.node[i]['type'] = 'focii'
        i = i+1

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
        if G.node[node]['type'] == 'person':
            arr_size.append(G.node[node]['name']*20)
        else:
            arr_size.append(1000)
    return arr_size

#extracting color for the different type of nodes
def extract_color(G):
    arr_color = []
    for node in G.nodes():
        if G.node[node]['type'] == 'person':
            arr_color.append('blue')
        else:
            arr_color.append('red')
    return arr_color
#extracting person nodes
def get_person_nodes(G):
    person = []
    for node in G.nodes():
        if G.node[node]['type'] == 'person':
            person.append(node)
    return person

#extracting focii nodes
def get_focii_nodes(G):
    focii = []
    for node in G.nodes():
        if G.node[node]['type'] == 'focii':
            focii.append(node)
    return focii
#linking focii to the nodes 
def connect_focii_nodes(G):
    person_nodes = get_person_nodes(G)
    focii_nodes = get_focii_nodes(G)
    for node in person_nodes:
        r = random.choice(focii_nodes)
        G.add_edge(node,r)
#plotting the graph
def plot_graph(G,labeldict,color,size):
    nx.draw(G,labels=labeldict ,node_color = color,node_size=size)
    plt.show()        


G = create_network()
assign_random_BMI(G)
add_focii(G)
connect_focii_nodes(G)
dict_label = extract_labels(G)
arr_size = extract_size(G)
color = extract_color(G)
plot_graph(G,dict_label,color,arr_size)
