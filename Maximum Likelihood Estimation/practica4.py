# -*- coding: utf-8 -*-
'''
    Representacion del Conocimiento
        Practica 4
            Algoritmo de Chow-Liu
        
    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''

import numpy as np
import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from math import log2
import time


# Given a dictionary (var: list of possible values), generates a numpy matrix
# with all possible combinations
def generateCombinationTable(values):
    
    # Calculate number of rows
    rows = 1
    for v in values.values():
        rows *= len(v)

    # Sort variables by lenght of range of values they can take
    sortedVars = [k for k in sorted(values, key=lambda k: len(values[k]), reverse=True)]

    # Create new table
    newTable = np.empty([len(sortedVars), rows], dtype=int)
    
    # Generate combinations
    first = True
    i = 0
    for var in sortedVars:
        l = []
        if first:
            consecutive = (rows / len(values[var]))
            first = False
        else:
            consecutive = consecutive / len(values[var])
        j = 0
        counter = 0
        for val in range(rows):
            if counter == consecutive:
                j += 1
                j = j % len(values[var])
                counter = 0
            l.append(sorted(values[var])[j])
            counter += 1
        
        newTable[i] = l
        i += 1
        
    newTable = np.transpose(newTable)   
    
    # Add header
    header = np.array([var for var in sortedVars])
    newTable = np.vstack([header, newTable])
    
    return newTable



# Generates a txt file containing example data
# values: list(dictionary, int). If set, a file of random data is generated based on the possible
#         values for each variable and the max number of samples.
# table: numpy matrix of combinations + counting. If set, data is generated following the count of each combination.
def generateData(fileName, values=[{}, 0], table=[]):
    
    vals = values[0]
    nSamples = values[1]
    
    f = open(fileName, "w")
    
    # Generate random data based on values
    if nSamples != 0:
        while nSamples > 0:
            sample = ""
            for v in vals:
                sample += v + str(random.choice(list(vals[v]))) + ','
            sample = sample[:-1] + '\n'
            f.write(sample)
            nSamples -= 1
            
    
    # Generate data based on counting table
    else:
        
        index = {i: var for i, var in enumerate(table[0])}
        for row in table[1:]:
            
            # Get combination
            sample = ""
            for i in range(len(row[:-1])):
                sample += str(index[i]) + str(row[i]) + ','
            sample = sample[:-1] + '\n'
            
            # Write combination N times
            for i in range(int(row[-1])):
                f.write(sample)

    f.close()



# Reads data from file
# Returns a dict with the count of samples of each type ((a0, b0, c0): 24, ...)
def readData(fileName):
    
    counting = {}
    
    f = open(fileName, "r")
    
    for sample in f:
        
        # Get combination
        comb = sample.split("\n")
        comb = tuple(comb[0].split(","))
        
        # Add combination to dictionary
        if comb not in counting:
            counting[comb] = 1
        else:
            counting[comb] += 1
        
    f.close()
    
    return counting
      

# Decomposes the counting in counts of single variables, pairs and global counts
# Ex: (a0,b0,c0:24) ---> (a0:24),(b0:24),(c0:24),(a0,b0:24),(b0,c0:24),(a:24),(b:24),(c:24)
# Pairs are stored in aplhabetical order left -> right
def decomposeCounting(counting):
    
    valueCount = {}
    globalCount = {}
    
    for comb in counting:
        
        # Add single vars
        for var in comb:
            # With values
            if var not in valueCount:
                valueCount[var] = counting[comb]
            else:
                valueCount[var] += counting[comb]
                
            # Global
            if var[0] not in globalCount:
                globalCount[var[0]] = counting[comb]
            else:
                globalCount[var[0]] += counting[comb]
        
        
        pairs = list(itertools.combinations(comb, 2))
        for pair in pairs:
            # With values
            if pair not in valueCount:
                valueCount[pair] = counting[comb]
            else:
                valueCount[pair] += counting[comb]
                
            # Global
            pair = (pair[0][0], pair[1][0])
            if pair not in globalCount:
                globalCount[pair] = counting[comb]
            else:
                globalCount[pair] += counting[comb]
                
    return valueCount, globalCount
            
 
# Returns the set of variables in the scope (a, b, c)
def getVars(dictionary):
    
    variables = set()
    
    for comb in dictionary:
        for var in comb:
            variables.add(var[0])
        
    return variables
    
    
# Given the count of samples, returns the probabilities for each variable/pair
def probabilitiesFromCounting(counting):
                            
    tables = {}
    valueCount, globalCount = decomposeCounting(counting)
    
    # Calculate probabilities
    for var in globalCount:
        
        # Single vars
        if not isinstance(var, tuple):
            p = np.matrix([var, 'z'])
            for v in valueCount:
                if not isinstance(v, tuple) and v[0] == var:
                    prob =  valueCount[v] / globalCount[v[0]]
                    p = np.vstack([p, [v[1], prob]])
            
        # Pairs
        else:
            first = var[0]
            second = var[1]
            p = np.matrix([first, second, 'z'])
            for v in valueCount:
                if isinstance(v, tuple) and (v[0][0], v[1][0]) == var:
                    prob =  valueCount[v] / globalCount[(v[0][0], v[1][0])]
                    p = np.vstack([p, [v[0][1], v[1][1], prob]])
        
        tables[var] = p

    return tables


# Given the combined probabilities of two variables and their single probailities,
# calculates the weight of the edge between both.
def mutualInformation(p_xy, p_x, p_y):

    p_x_dict = dict(p_x[1:])
    p_y_dict = dict(p_y[1:])
    weight = 0

    for row in p_xy[1:]:
        denom = 1
        for i, value in enumerate(row[:-1]):
            if p_xy[0][i] == p_x[0][0]:
                denom *= float(p_x_dict.get(value, 0))
            else:
                denom *= float(p_y_dict.get(value, 0))

        weight += float(row[-1]) * log2(float(row[-1]) / (denom))

    return weight
            


# Given the nodes of a complete graph and the table of probabilities
# for each node/node pair, builds a weightes graph following
# Chow-Liu algorithm's formula
def buildWeightedGraph(variables, probabilities):

    # Create all possible undirected edges (complete graph)
    k = nx.complete_graph(variables, nx.Graph)

    for edge in k.edges:
        
        node1, node2 = edge
        
        p_x = probabilities[node1]
        p_y = probabilities[node2]
        
        if edge in probabilities:
            p_xy = probabilities[edge]
        else:
            p_xy = probabilities[tuple(list(edge)[::-1])]
        #start = time.time()
        mi = mutualInformation(np.array(p_xy), np.array(p_x), np.array(p_y))
        #end = time.time()
        k.add_edge(node1, node2, weight=mi)
    
    #total = end - start

    return k 

        
# Given a graph, it returns the spanning tree of maximum weight using
# Kruskal's algorithm.
def maxSpanningTree(graph):

    # Obtener todas las aristas ordenadas por peso en orden descendente
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)
    
    # Inicializar un diccionario para rastrear los conjuntos de nodos
    sets = {node: {node} for node in graph.nodes}
    
    # Inicializar el árbol de recubrimiento máximo
    max_spanning_tree = nx.Graph()
    
    for edge in edges:
        u, v, weight = edge
        set_u = sets[u]
        set_v = sets[v]
        
        # Verificar si u y v están en conjuntos diferentes (evitar ciclos)
        if set_u != set_v:
            max_spanning_tree.add_edge(u, v, weight=weight['weight'])
            
            # Unir los conjuntos de u y v
            new_set = set_u.union(set_v)
            #print(new_set)
            for node in new_set:
                sets[node] = new_set
    
    return max_spanning_tree


# Given a tree, a random node is picked as root and
# outward directionality is applied
def outwardDirectionality(tree):
    
    newTree = nx.DiGraph()
    queue = [random.choice(list(tree.nodes))]
    visited = set()

    
    while queue:
        v = queue.pop(0) # deletes and returns the first element of the list
        
        # Vertex added to list when visited
        if v not in visited:
            visited.add(v)
            
            # Apply directionality and add children to the queue
            for neighbor in list(tree.neighbors(v)):
                if neighbor not in visited:
                    edge_weight = tree[v][neighbor]['weight']
                    newTree.add_edge(v, neighbor, weight=edge_weight)
                queue.append(neighbor)
 
    return newTree
    


def chowLiu(sampleFile):

    # Count of samples
    counting = readData(sampleFile)

    # Calculate probabilities
    tables = probabilitiesFromCounting(counting)

    # Make weighted graph
    start1 = time.time()
    weightedGraph = buildWeightedGraph(getVars(counting), tables)
    end1 = time.time() - start1
    
    # Maximum spanning tree
    start2 = time.time()
    tree = maxSpanningTree(weightedGraph)
    end2 = time.time() - start2
    
    # Apply directionality
    start3 = time.time()
    tree = outwardDirectionality(tree)
    end3 = time.time() - start3

    
    elapsed_time = time.time() - start1

    return tree, [elapsed_time, end1, end2, end3]



