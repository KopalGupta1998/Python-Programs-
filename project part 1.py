"""
This program is written to implement the 
ER algorithm.
"""
import random
import simpleplot
def build_random_graph(num_nodes,p):
    ver=range(num_nodes)
    edges=[]
    subsets=[]
    graph={}
    for i in ver:
        for j in ver:
            if i!=j:
                subsets.append((i,j))
    #print len(subsets)
    #print subsets
    for edge in subsets:
        a=random.random()
        if a<p and edge not in edges:
            edges.append(edge)
    for node in ver:
        graph[node]=set([])
    for node in ver:
        for edge in edges:
            if edge[0]==node:
                graph[node].add(edge[1])
    return graph
def compute_in_degrees(digraph):
    dicstr=dict()
    for i in digraph:
        dicstr[i]=0
    for nodes in digraph:
        for node in digraph[nodes]:
            dicstr[node]+=1
    return dicstr
def in_degree_distribution(digraph):
    distr=dict()
    digraph=compute_in_degrees(digraph)
    for i in digraph.values():
        distr[i]=0
    nodes=len(digraph.keys())
    for node in digraph:
        distr[digraph[node]]=distr[digraph[node]]+1
    for node in distr:
        distr[node]=float(distr[node])/nodes
    return distr
#print compute_in_degrees(build_random_graph(5,0.5))
plot1= in_degree_distribution(build_random_graph(10,0.5))
plot2=in_degree_distribution(build_random_graph(6,0.8))
#plot3=in_degree_distribution(build_random_graph(10,1))


simpleplot.plot_lines("Sample",400,300,"x","y",[plot1,plot2])