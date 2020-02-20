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
"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
def UPA_Graph(n,m):
    V=range(m)
    upa_graph={0: set([1, 2]), 1: set([2,0]), 2: set([0,1])}
    graph=UPATrial(m)
    for i in range(m ,n):
        neighbors=graph.run_trial(m)
        V.append(i)
        upa_graph[i]=neighbors
    return upa_graph


def build_random_graph(num_nodes,p):
    ver=range(num_nodes)
    edges=[]
    subsets=[]
    graph={}
    for i in ver:
        for j in range(i,num_nodes):
            if i!=j:
                subsets.append((i,j))
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
                graph[edge[1]].add(edge[0])
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
graph=UPA_Graph(1239,3)
for node in graph:
    for n in graph:
        if node in graph[n]:
            graph[node].add(n)
print graph
l=[]
attack_order=random_order(graph)
print attack_order
obj=resilience(graph,attack_order)
for r in obj:
    l.append(r)
print l



    
    
    





