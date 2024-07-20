# -*- coding: utf-8 -*-
'''
    Representación del Conocimiento
        Practica 3
            Test Inferencia probabilistica

    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''

import practica_3 as p3
import networkx as nx
import numpy as np
import time


#FUNCION QUE COMPRUEBA SI AMBAS TABLAS SON IGUALES
def checkElement(result, originalResult):
    for i in range(len(originalResult)):
        for j in range(len(originalResult[i])):
            originalElement = originalResult[i][j]
            resultElement = result[i][j]
            if (originalElement != resultElement):
                difference = abs(originalElement - float(resultElement))
                if (difference >= 1e-2):
                    return False
    return True

#EV PARA INFERENCIA MARGINAL
def marginal():
    graph = nx.DiGraph()
    graph.add_edge("D", "A")
    graph.add_edge("A", "B")
    graph.add_edge("E", "A")
    graph.add_edge("E", "C")

    factors = {}
    factors["A"] = p3.Factor(np.array([["A", "D", "E", "p"],
                [0, 0, 0, 0.3],
                [0, 0, 1, 0.1],
                [0, 1, 0, 0.7],
                [0, 1, 1, 0.2],
                [1, 0, 0, 0.4],
                [1, 0, 1, 0.2],
                [1, 1, 0, 0.2],
                [1, 1, 1, 0.3],
                [2, 0, 0, 0.3],
                [2, 0, 1, 0.7],
                [2, 1, 0, 0.1],
                [2, 1, 1, 0.5]]))

    factors["B"] = p3.Factor(np.array([["A", "B", "p"],
                [0, 0, 0.7],
                [0, 1, 0.3],
                [1, 0, 0.4],
                [1, 1, 0.6],
                [2, 0 ,0.1],
                [2, 1, 0.9]]))

    factors["C"] = p3.Factor(np.array([["C", "E", "p"],
                [0, 0, 0.6],
                [0, 1, 0.3],
                [1, 0, 0.1],
                [1, 1, 0.3],
                [2, 0 ,0.4],
                [2, 1, 0.3]]))

    factors["D"] = p3.Factor(np.array([["D", "p"],
                [0, 0.6],
                [1, 0.4]]))

    factors["E"] = p3.Factor(np.array([["E", "p"],
                [0, 0.8],
                [1, 0.2]]))

    nx.set_node_attributes(graph, factors, "factor")



    ################################################# TEST #################################################
    count = 100
    suma = 0
    for i in range(count):
        startTime = time.perf_counter()
        x = p3.variableElimination(graph, "B", {}, ["D", "E", "C", "A"])

        endTime = time.perf_counter()

        execution_time = endTime - startTime
        suma += execution_time

    print(f"1. Tiempo de ejecución: {float(suma / count)} segundos")

    originalResult = ([["B", "p"],
                [0, 0.4288],
                [1, 0.5712]])

    if (checkElement(x.table, originalResult)):
        print("Pasa todos los test de forma correcta")
    else:
        print("Hay algun error")


    ###########################################################################################
    suma = 0
    for i in range(count):
        startTime = time.perf_counter()
        x = p3.variableElimination(graph, "B", {}, ["C", "E", "D", "A"])
        endTime = time.perf_counter()
        execution_time = endTime - startTime
        suma += execution_time

    print(f"2. Tiempo de ejecución: {float(suma / count)} segundos")

    if (checkElement(x.table, originalResult)):
        print("Pasa todos los test de forma correcta")
    else:
        print("Hay algun error")

# ###########################################################################################



# ###################################################################################################################################################
# #EV PARA INFERENCIA CONDICIONAL
def conditional():
    graph2 = nx.DiGraph()
    graph2.add_edge("A", "C")
    graph2.add_edge("A", "D")
    graph2.add_edge("B", "E")
    graph2.add_edge("B", "D")
    graph2.add_edge("C", "F")
    graph2.add_edge("D", "F")

    factors = {}
    factors["F"] = p3.Factor(np.array([["C", "D", "F", "p"],
                [0, 0, 0, 0.6],
                [0, 0, 1, 0.2],
                [0, 0, 2, 0.2],
                [0, 1, 0, 0.5],
                [0, 1, 1, 0.3],
                [0, 1, 2, 0.2],
                [0, 2, 0, 0.4],
                [0, 2, 1, 0.3],
                [0, 2, 2, 0.3],
                [1, 0, 0, 0.5],
                [1, 0, 1, 0.2],
                [1, 0, 2, 0.3],
                [1, 1, 0, 0.3],
                [1, 1, 1, 0.3],
                [1, 1, 2, 0.4],
                [1, 2, 0, 0.1],
                [1, 2, 1, 0.4],
                [1, 2, 1, 0.5]]))

    factors["D"] = p3.Factor(np.array([["A", "B", "D", "p"],
                [0, 0, 0, 0.8],
                [0, 0, 1, 0.1],
                [0, 0, 2, 0.1],
                [0, 1, 0, 0.7],
                [0, 1, 1, 0.2],
                [0, 1, 2, 0.1],
                [0, 2, 0, 0.6],
                [0, 2, 1, 0.2],
                [0, 2, 2, 0.2],
                [1, 0, 0, 0.7],
                [1, 0, 1, 0.1],
                [1, 0, 2, 0.2],
                [1, 1, 0, 0.5],
                [1, 1, 1, 0.2],
                [1, 1, 2, 0.3],
                [1, 2, 0, 0.3],
                [1, 2, 1, 0.3],
                [1, 2, 2, 0.4]]))

    factors["C"] = p3.Factor(np.array([["A", "C", "p"],
                [0, 0, 0.8],
                [0, 1, 0.2],
                [1, 0, 0.6],
                [1, 1, 0.4]]))

    factors["E"] = p3.Factor(np.array([["B", "E", "p"],
                [0, 0, 0.6],
                [0, 1, 0.4],
                [1, 0, 0.6],
                [1, 1, 0.4],
                [2, 0, 0.4],
                [2, 1, 0.6]]))

    factors["A"] = p3.Factor(np.array([["A", "p"],
                [0, 0.6],
                [1, 0.4]]))

    factors["B"] = p3.Factor(np.array([["B", "p"],
                [0, 0.4],
                [1, 0.4],
                [2, 0.2]]))

    nx.set_node_attributes(graph2, factors, "factor")

    ############################################################################################
    count = 100
    suma = 0
    for i in range(count):
        startTime = time.perf_counter()

        y = p3.variableElimination(graph2, "F",  {'B': 2, 'D': 1}, ["E", "A", "C"])
        endTime = time.perf_counter()

        execution = endTime - startTime
        suma += execution

    print(f"3. Tiempo de ejecución: {float(suma / count)} segundos")

    originalResult = ([["F", "p"],
                [0, 0.44],
                [1, 0.30],
                [2, 0.26]])

    if (checkElement(y.table, originalResult)):

        print("Pasa todos los test de forma correcta")
    else:
        print("Hay algun error")

    ############################################################################################

    suma = 0
    for i in range(count):
        startTime = time.perf_counter()
        y = p3.variableElimination(graph2, "F",  {'D': 1, 'E': 1}, ["B", "A", "C"])
        endTime = time.perf_counter()

        execution = endTime - startTime
        suma += execution
        
    print(f"4. Tiempo de ejecución: {float(suma / count)} segundos")

    originalResult = ([["F", "p"],
                [0, 0.44],
                [1, 0.30],
                [2, 0.26]])

    if (checkElement(y.table, originalResult)):
        print("Pasa todos los test de forma correcta")
    else:
        print("Hay algun error")
        
        
    ############################################################################################

    suma = 0
    for i in range(count):
        startTime = time.perf_counter()
        y = p3.variableElimination(graph2, "F",  {'A': 0}, ["E", "B", "C", "D"])
        endTime = time.perf_counter()

        execution = endTime - startTime
        suma += execution
        
    print(f"5. Tiempo de ejecución: {float(suma / count)} segundos")
        
        
    ############################################################################################

    suma = 0
    for i in range(count):
        startTime = time.perf_counter()
        y = p3.variableElimination(graph2, "F",  {'A': 0}, ["E", "D", "C", "B"])
        endTime = time.perf_counter()

        execution = endTime - startTime
        suma += execution
        
    print(f"6. Tiempo de ejecución: {float(suma / count)} segundos")
    
    
    y = p3.variableElimination(graph2, "E",  {'C': 1, 'D':1, 'F':1}, ["B", "A"])
    print(y.table)


marginal()
conditional()