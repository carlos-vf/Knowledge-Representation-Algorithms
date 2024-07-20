# -*- coding: utf-8 -*-
'''
    Representacion del Conocimiento
        Practica 4
            Algoritmo de Chow-Liu
            Test de pruebas
        
    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''

import practica4 as p4
import numpy as np

import networkx as nx
import matplotlib.pyplot as plt
from math import log2


def example1(count):
    # Possible values for each variable
    values = {"a":{0, 1},
            "b":{0, 1},
            "c":{0, 1}}

    # Table made of value combinations and their count
    table = p4.generateCombinationTable(values)
    c = ["z", 24,36,12,28,12,28,12,48]
    table = np.c_[ table, np.array(c) ]

    # Data generation
    p4.generateData("data.txt", table=table)

    # Chow-Liu
    tree, time = p4.chowLiu("data.txt")
    accTotal = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    for i in range(count):
        tree, time = p4.chowLiu("data.txt")
        accTotal += time[0]
        acc1 += time[1]
        acc2 += time[2]
        acc3 += time[3]

    res = float(accTotal/count)
    print("Tiempo de ejecucion ejemplo 1: ", res)
    print("Paso 1: ", acc1/count)
    print("Paso 2: ", acc2/count)
    print("Paso 3: ", acc3/count)
    # # Plot the graph
    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', font_color='black', edge_color='gray', font_size=8)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
    plt.show()



def example2(count):
    # Possible values for each variable
    values = {"a":{0, 1, 2},
            "b":{0, 1, 2},
            "c":{0, 1, 2}}

    # Table made of value combinations and their count
    table = p4.generateCombinationTable(values)
    c = ["z", 24,36,12,28,12,28,12,48,24,36,12,28,12,28,12,48,24,36,12,28,12,28,12,48,36,24,28]
    table = np.c_[ table, np.array(c) ]


    # Data generation
    p4.generateData("data.txt", table=table)

    # Chow-Liu
    tree, time = p4.chowLiu("data.txt")
    accTotal = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    for i in range(count):
        tree, time = p4.chowLiu("data.txt")
        accTotal += time[0]
        acc1 += time[1]
        acc2 += time[2]
        acc3 += time[3]

    res = float(accTotal/count)
    print("Tiempo de ejecucion ejemplo 2: ", res)
    print("Paso 1: ", acc1/count)
    print("Paso 2: ", acc2/count)
    print("Paso 3: ", acc3/count)
    # # Plot the graph
    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', font_color='black', edge_color='gray', font_size=8)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
    plt.show()

 
def example3(count):
    # Possible values for each variable
    values = {"a":{0, 1},
            "b":{0, 1},
            "c":{0, 1},
            "d":{0, 1}}

    # Table made of value combinations and their count
    table = p4.generateCombinationTable(values)
    c = ["z", 24,36,12,28,12,28,12,48,15,3,42,8,19,7,31,9]
    table = np.c_[ table, np.array(c) ]

    # Data generation
    p4.generateData("data.txt", table=table)

    # Chow-Liu
    tree, time = p4.chowLiu("data.txt")
    accTotal = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    for i in range(count):
        tree, time = p4.chowLiu("data.txt")
        accTotal += time[0]
        acc1 += time[1]
        acc2 += time[2]
        acc3 += time[3]

    res = float(accTotal/count)
    print("Tiempo de ejecucion ejemplo 3: ", res)
    print("Paso 1: ", acc1/count)
    print("Paso 2: ", acc2/count)
    print("Paso 3: ", acc3/count)
    # # Plot the graph
    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', font_color='black', edge_color='gray', font_size=8)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
    plt.show()
    
    

 
def example4(count):
    # Possible values for each variable
    values = {"a":{0, 1},
            "b":{0, 1},
            "c":{0, 1},
            "d":{0, 1},
            "e":{0, 1},
            "f":{0, 1},
            "g":{0, 1},
            "h":{0, 1},
            "i":{0, 1},
            "j":{0, 1}}

    # Data generation
    p4.generateData("data.txt", values=[values, 300])

    # Chow-Liu
    tree, time = p4.chowLiu("data.txt")
    accTotal = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    for i in range(count):
        tree, time = p4.chowLiu("data.txt")
        accTotal += time[0]
        acc1 += time[1]
        acc2 += time[2]
        acc3 += time[3]

    res = float(accTotal/count)
    print("Tiempo de ejecucion ejemplo 4: ", res)
    print("Paso 1: ", acc1/count)
    print("Paso 2: ", acc2/count)
    print("Paso 3: ", acc3/count)

    # # Plot the graph
    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', font_color='black', edge_color='gray', font_size=8)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
    plt.show()
    
    
    
def example5(count):
    # Possible values for each variable
    values = {"a":{0, 1},
            "b":{0, 1},
            "c":{0, 1},
            "d":{0, 1},
            "e":{0, 1},
            "f":{0, 1},
            "g":{0, 1},
            "h":{0, 1},
            "i":{0, 1},
            "j":{0, 1},
            "k":{0, 1},
            "l":{0, 1},
            "m":{0, 1},
            "n":{0, 1},
            "o":{0, 1},
            "p":{0, 1},
            "q":{0, 1},
            "r":{0, 1},
            "s":{0, 1},
            "t":{0, 1}}

    # Data generation
    p4.generateData("data.txt", values=[values, 300])

    # Chow-Liu
    tree, time = p4.chowLiu("data.txt")
    accTotal = 0
    acc1 = 0
    acc2 = 0
    acc3 = 0
    for i in range(count):
        tree, time = p4.chowLiu("data.txt")
        accTotal += time[0]
        acc1 += time[1]
        acc2 += time[2]
        acc3 += time[3]

    res = float(accTotal/count)
    print("Tiempo de ejecucion ejemplo 5: ", res)
    print("Paso 1: ", acc1/count)
    print("Paso 2: ", acc2/count)
    print("Paso 3: ", acc3/count)

    # # Plot the graph
    pos = nx.spring_layout(tree)
    nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', font_color='black', edge_color='gray', font_size=8)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
    plt.show()
    
 

count = 100

# n = 3, k = 2
example1(count)

# n = 3, k = 3
example2(count)

# n = 4, k = 2
example3(count)

# n = 10, k = 2
example4(count)

# n = 20, k = 2
example5(count)
