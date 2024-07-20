# -*- coding: utf-8 -*-
'''
    Representacion del Conocimiento
        Practica 2
            Separacion Grafica
        
    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''

import networkx as nx
import matplotlib.pyplot as plt
import copy


DG = nx.DiGraph()
DG.add_edge('A', 'C')
DG.add_edge('A', 'D')
DG.add_edge('B', 'D')
DG.add_edge('B', 'E')
DG.add_edge('C', 'F')
DG.add_edge('D', 'F')
DG.add_edge('D', 'G')


# graph: initial directed graph
# v1: first vertex
# v2: second vertex
# observed: list of observerd vertices
# Returns True if v1 and v2 are independent given obbserved;
# False if not
def graphicSeparation(graph, v1, v2, observed):
    
    # Delete leaves
    cantDelete = copy.deepcopy(observed)
    cantDelete.add(v1)
    cantDelete.add(v2)
    newGraph = deleteLeaves(graph, leaves(graph), cantDelete)
    
    # Moralize the graph
    moralizedGraph = moralize(newGraph)
    
    # Delete observed vertices
    for v in observed:
        moralizedGraph.remove_node(v)
    
    # Check if there is a path between v1 and v2 avoiding observed
    p = existsPath(moralizedGraph, v1, v2)
    
    return (not p), moralizedGraph



# Returns a list with all leaf nodes from the graph
def leaves(graph):
    
    # Identify and return a list of leaf vertices
    leaf_vertices = [v for v in graph.nodes() if not list(graph.successors(v))]
    
    return leaf_vertices



# Deletes all leaf node from the graph
# When a vertex is deleted, it checks if parents are leaves and deletes them if so    
def deleteLeaves(graph, leavesList, cantDelete):
    
    newGraph = copy.deepcopy(graph)
    
    # As long as there are vertices to be removed in the list
    while leavesList:
        
        # Take the first vertex from the list
        vertex = leavesList.pop(0)
        
        # If the vertex is not in the list of observed vertices
        if vertex not in cantDelete:
        
            # Get the predecessors (parent vertices) of the vertex
            predecessors = list(newGraph.predecessors(vertex))
           
            # Remove the vertex itself from the graph
            newGraph.remove_node(vertex)
            
            for parent_vertex in predecessors:

                # If the parent vertex has no successors, i.e., it has become a leaf node
                if not list(newGraph.successors(parent_vertex)):
                    
                    # Add the parent vertex to the list of vertices to be removed
                    leavesList.append(parent_vertex)
    
    return newGraph
                    

                
# graph: graph to be moralized
# Returns a graph where:
#   - Parents with common child are connected
#   - Edges have no direction (undirected graph)
def moralize(graph):
    vertices = graph.nodes
    edges= graph.edges
    parents = {}
    newEdges = set()
    
    # Parents dictionary
    # key, value = child, parent
    for v in vertices:
        p = list(graph.predecessors(v))
        parents[v] = p

        
    # Add edges between parents with common children
    for common in parents.values():
        if len(common) > 1:
            for p in common:
                for otherPs in common:
                    e = (p, otherPs)
                    if p != otherPs and e not in newEdges:
                        newEdges.add(e)
                        

    # Create undirected graph
    undirectedGraph = nx.Graph()
    for v in vertices:
        undirectedGraph.add_node(v)
    for e in edges:
        undirectedGraph.add_edge(e[0], e[1])
    for e in newEdges:
        undirectedGraph.add_edge(e[0], e[1])
        
    return undirectedGraph

	

# Searches for a path between origin and end nodes
# It uses Breadth First Search
# Returns True if a path exists; False if not
def existsPath(graph, origin, end):
    
    queue = [origin]
    visited = set()
    
    while queue:
        v = queue.pop(0) # deletes and returns the first element of the list
        
        # Vertex added to list when visited
        if v not in visited:
            visited.add(v)
            
            # If end is reached, there is a path
            if v == end:
                return True
            
            # Else, add children to the queue
            for neighbor in list(graph.neighbors(v)):
                queue.append(neighbor)
 
    return False

