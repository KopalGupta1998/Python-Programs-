"""
The implementation of Project 2.
"""
import poc_queue 
import random
#import user46_yYCllkbTXS_0 as test
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

def cc_visited(ugraph):
    """
    This function asserts the connected components 
    of the graph
    """
    vertices=ugraph.keys()
    connected=[]
    while len(vertices)!=0:
        selected=random.choice(vertices)
        visited=bfs_visited(ugraph,selected)
        if visited not in connected:
            connected.append(visited)
        vertices.remove(selected)
    return connected
        
def largest_cc_size(ugraph):
    """
    This function returns the size 
    of the largest connected component.
    """
    connected_component=cc_visited(ugraph)
    largest_size=0
    for connected in connected_component:
        if len(connected)>largest_size:
            largest_size=len(connected)
    return largest_size

def compute_resilience(ugraph,attack_order):
    """
    This function computes the resilience 
    of the graph.
    """
    largest_size=[largest_cc_size(ugraph)]
    for order in attack_order:
        ugraph.pop(order)
        for node in ugraph:
            if order in ugraph[node]:
                ugraph[node].remove(order)
        largest_size.append(largest_cc_size(ugraph))
    return largest_size

#print compute_resilience(test.GRAPH0,[1,2])
