"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(30)
import math
import simpleplot
class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]
        

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def DPA_Graph(n,m):
    V=range(m)
    dpa_graph={0: set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1: set([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 2: set([0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 3: set([0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11]), 4: set([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11]), 5: set([0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]), 6: set([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]), 7: set([0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]), 8: set([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]), 9: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]), 10: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]), 11: set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}
    graph=DPATrial(m)
    for i in range(m ,n):
        neighbors=graph.run_trial(m)
        V.append(i)
        dpa_graph[i]=neighbors
    return dpa_graph

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
#print sum(in_degree_distribution(DPA_Graph(27770,12)).values())
def build_plot():
    plot={}
    digraph=in_degree_distribution(DPA_Graph(27770,12))
    for node in digraph:
        if node!=0:
            plot[math.log(node,10)]=math.log(digraph[node],10)
    return plot

plot1=build_plot()
print plot1
simpleplot.plot_scatter("log/log plot of in_degree_distribution of DPA_graph",600,600,"Number of edges","Fraction of nodes",[plot1])

