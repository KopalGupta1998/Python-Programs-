"""
This is a program to construct a complete graph 
when the number of nodes is given.
"""
EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),
           7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    This function construct a complete graph 
    based on the number of nodes entered.
    """
    complete_graph={}
    nodes_copy=range(num_nodes)
    for node_idx in nodes_copy:
        neighbors=[]
        for neighbor in nodes_copy:
            if node_idx!=neighbor:
                neighbors.append(neighbor)
        complete_graph[node_idx]=set(neighbors)
    return complete_graph

def compute_in_degrees(digraph):
    """
    This function computes the number of in-degrees 
    of each node and stores them in a dictionary and
    returns that dictionary.
    """
    in_degrees={}
    in_degree=[]
    for node in digraph.keys():
        for neigh in digraph.keys():
            if node in digraph[neigh]:
                in_degree.append(digraph[neigh])
        in_degrees[node]=len(in_degree)
        in_degree=[]
    return in_degrees

def in_degree_distribution(digraph):
    """
    This function computes the in-degree distribution 
    of the graph
    """
    in_degrees=compute_in_degrees(digraph)
    items=[]
    degree_distribution={}
    for degree in in_degrees.values():
        if degree not in items:
            items.append(degree)
    for degree in items:
        num=0
        for in_degree in in_degrees.values():
            if in_degree==degree:
                num+=1
        if num!=0:
            degree_distribution[degree]=num
    return degree_distribution

print compute_in_degrees(EX_GRAPH0)
print in_degree_distribution(EX_GRAPH0)

        
        
        