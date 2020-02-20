"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import math
import simpleplot
# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

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
EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),
           7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

print sum(in_degree_distribution(citation_graph).values())
#print in_degree_distribution(citation_graph)

def build_plot():
    plot={}
    digraph=in_degree_distribution(citation_graph)
    for node in digraph:
        if node!=0:
            plot[math.log(node,10)]=math.log(digraph[node],10)
    return plot

plot1=build_plot()
print plot1
#simpleplot.plot_scatter("Sample",600,600,'x','y',[plot1])
