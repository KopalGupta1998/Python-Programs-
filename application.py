"""
Provided code for Application portion of Module 2
"""

# general imports
import urllib2
import random
import time
import math
import poc_queue

# CodeSkulptor import
#import simpleplot
import codeskulptor
codeskulptor.set_timeout(60)

# Desktop imports
#import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
def bfs_visited(ugraph,start_node):
    """
    This function computes the 
    order in which nodes are visted
    """
    
    queue=poc_queue.Queue()
    visited=set([start_node])
    queue.enqueue(start_node)
    while queue.__len__()!=0:
        node=queue.dequeue()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    return visited  

def connected_components(graph, nodes):
    """Given an undirected graph represented as a mapping from nodes to
    the set of their neighbours, and a set of nodes, find the
    connected components in the graph containing those nodes.

    Returns:
    - mapping from nodes to the canonical node of the connected
      component they belong to
    - mapping from canonical nodes to connected components

    """
    canonical = {}
    components = {}
    while nodes:
        node = nodes.pop()
        component = bfs_visited(graph, node)
        components[node] = component
        nodes.difference_update(component)
        for n in component:
            canonical[n] = node
    return canonical, components
def resilience(ugraph, attack_order):
    """Given an undirected graph represented as a mapping from nodes to
    an iterable of their neighbours, and an iterable of nodes, generate
    integers such that the the k-th result is the size of the largest
    connected component after the removal of the first k-1 nodes.

    """
    # Take a copy of the graph so that we can destructively modify it.
    graph = copy_graph(ugraph)
    canonical, components = connected_components(graph, set(graph))
    
    largest = lambda: max(map(len, components.values()))
    yield largest()
    for node in attack_order:
        # Find connected component containing node.
        component = components.pop(canonical.pop(node))

        # Remove node from graph.
        for neighbor in graph[node]:
            graph[neighbor].remove(node)
        graph.pop(node)
        component.remove(node)

        # Component may have been split by removal of node, so search
        # it for new connected components and update data structures
        # accordingly.
        canon, comp = connected_components(graph, component)
        for item in canon:
            canonical[item]=canon[item]
        for item in comp:
            components[item]=comp[item]
        if not graph:
            yield 0
        else:
            yield largest()
##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

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
    print edges
    for node in ver:
        graph[node]=set([])
    for node in ver:
        for edge in edges:
            if edge[0]==node:
                graph[node].add(edge[1])
    return graph
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
def random_order(ugraph):
    nodes=ugraph.keys()
    random.shuffle(nodes)
    return nodes
graph=build_random_graph(1289,0.004)
#attack_order=random_order(graph)
#obj=resilience(graph,attack_order)
#for r in obj:
   #print r



    
    
    





