# -*- coding: utf-8 -*-
'''
    Representacion del Conocimiento
        Practica 2
            Test Separacion Grafica

    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''
import practica2 as p2

def graph1():
    DG = p2.nx.DiGraph()
    DG.add_edge('A', 'C')
    DG.add_edge('A', 'D')
    DG.add_edge('B', 'D')
    DG.add_edge('B', 'E')
    DG.add_edge('C', 'F')
    DG.add_edge('D', 'F')
    DG.add_edge('D', 'G')

    # Print the original graph
    print("Original graph:")
    print("Nodes: ", DG.nodes)
    print("Edges: ", DG.edges)

    p2.plt.figure(figsize=(8, 8))
    pos = p2.nx.spring_layout(DG)
    p2.nx.draw(DG, pos, with_labels=True, node_size=700, node_color="skyblue")
    p2.plt.show()

    # Case 1: A _|_ G {B, D}:

    # Input
    X = 'A'
    Y = 'G'
    Z = {'B', 'D'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be TRUE"

    ###################################################################################################

    # Case 2: A _|_ B {C, E}:

    # Input
    X = 'A'
    Y = 'B'
    Z = {'C', 'E'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be TRUE"

    ###################################################################################################

    # Case 3: A _|_ E {C, D}:

    # Input
    X = 'A'
    Y = 'E'
    Z = {'C', 'D'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

    ###################################################################################################

    # Case 4: A _|_ G {B, C, F}:

    # Input
    X = 'A'
    Y = 'G'
    Z = {'B', 'C', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

def graph2():
    DG = p2.nx.DiGraph()
    DG.add_edge('A', 'B')
    DG.add_edge('B', 'C')
    DG.add_edge('B', 'D')
    DG.add_edge('C', 'E')
    DG.add_edge('D', 'E')
    DG.add_edge('E', 'F')

    # Print the original graph
    print("Original graph:")
    print("Nodes: ", DG.nodes)
    print("Edges: ", DG.edges)

    p2.plt.figure(figsize=(8, 8))
    pos = p2.nx.spring_layout(DG)
    p2.nx.draw(DG, pos, with_labels=True, node_size=700, node_color="skyblue")
    p2.plt.show()

    # Case 1: A _|_ F {B, C, D, E}:

    # Input
    X = 'A'
    Y = 'F'
    Z = {'B', 'C', 'D', 'E'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be TRUE"

    ###################################################################################################

    # Case 2: A _|_ D {C, E}:

    # Input
    X = 'A'
    Y = 'D'
    Z = {'C', 'E'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

    ###################################################################################################

    # Case 3: B _|_ F {A, C, D, E}:

    # Input
    X = 'B'
    Y = 'F'
    Z = {'A', 'C', 'D', 'E'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be TRUE"

    ###################################################################################################

    # Case 4: B _|_ C {A, D, E, F}:

    # Input
    X = 'B'
    Y = 'C'
    Z = {'A', 'D', 'E', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

def graph3():
    DG = p2.nx.DiGraph()
    DG.add_edge('A', 'B')
    DG.add_edge('A', 'C')
    DG.add_edge('B', 'D')
    DG.add_edge('C', 'E')
    DG.add_edge('D', 'F')
    DG.add_edge('E', 'F')

    # Print the original graph
    print("Original graph:")
    print("Nodes: ", DG.nodes)
    print("Edges: ", DG.edges)

    p2.plt.figure(figsize=(8, 8))
    pos = p2.nx.spring_layout(DG)
    p2.nx.draw(DG, pos, with_labels=True, node_size=700, node_color="skyblue")
    p2.plt.show()

    # Case 1: A _|_ E {B, C, D, F}:

    # Input
    X = 'A'
    Y = 'E'
    Z = {'B', 'C', 'D', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be TRUE"

    ###################################################################################################

    # Case 2: B _|_ C {A, D, E, F}:

    # Input
    X = 'B'
    Y = 'C'
    Z = {'A', 'D', 'E', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert result, "The result is incorrect, it should be FALSE"

    ###################################################################################################

    # Case 3: D _|_ E {A, B, C, F}:

    # Input
    X = 'D'
    Y = 'E'
    Z = {'A', 'B', 'C', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

    ###################################################################################################

    # Case 4: C _|_ E {B, D, F}:

    # Input
    X = 'C'
    Y = 'E'
    Z = {'B', 'D', 'F'}

    # Output
    result, g = p2.graphicSeparation(DG, X, Y, Z)

    print("\nResulting graph:")
    print("Nodes: ", g.nodes)
    print("Edges: ", g.edges)

    # Result
    print("Is " + X + " independent of " + Y + " given " + str(Z) + "?: " + str(result))
    assert not result, "The result is incorrect, it should be FALSE"

print("### GRAPH 1 ###")
print()
graph1()
print()
print("### GRAPH 2 ###")
print()
graph2()
print()
print("### GRAPH 3 ###")
print()
graph3()
print()
print("ALL TESTS HAVE PASSED SUCCESSFULLY FOR EACH GRAPH")
