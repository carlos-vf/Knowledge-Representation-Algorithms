# -*- coding: utf-8 -*-


import networkx as nx
import numpy as np
import copy


class Factor:
    
    def __init__(self, phi):
        
        self.table = phi
        
        # Scope: set of variables
        self.scope = set()
        for v in phi[0]:
            if v != 'p':
                self.scope.add(v)
                
        # Values: dict(var, list of values)
        self.values = {}
        self.rows = np.shape(phi)[0]
        self.columns = np.shape(phi)[1]

        for j in range(self.columns - 1):
            var = phi[0][j]
            self.values[var] = set()
            for i in range(1, self.rows):
                self.values[var].add(phi[i][j])
            

    def product(self, phi):

        # Generate a table with all possible combinations of values for variables in 'newScope'.
        newValues = copy.deepcopy(self.values)  # Copy values from 'self'
        newValues.update(phi.values)  # Add values from 'phi'
        newTable = self.generateCombinationTable(newValues)

        # Create dictionaries to map variables to indices in the tables
        selfIndices = {var: i for i, var in enumerate(self.table[0]) if var != 'p'}
        phiIndices = {var: i for i, var in enumerate(phi.table[0]) if var != 'p'}
        newIndices = {var: i for i, var in enumerate(newTable[0]) if var != 'p'}

        newTable = np.column_stack((newTable, np.ones(len(newTable), dtype=float)))
        newTable[0][-1] = 'p'  # Label the column as 'p'

        # Iterate through the table of the first factor and update the newTable
        for selfRow in self.table[1:]:
            #selfVarValues = selfRow[:-1]  # Variable values in the current row
            selfPValue = selfRow[-1]  # Probability value
            for index in range(1, len(newTable)):  # Start from 1 to skip the header row
                coicidence = True
                for var in self.scope:
                    if (selfRow[selfIndices[var]] != newTable[index][newIndices[var]]):
                        coicidence = False
                        break
                if coicidence:
                    # Copy the probability value from self.table to newTable
                    newTable[index][-1] = selfPValue
        
        #Iterate through the table of the second factor and update the new table by multiplying probabilities
        for row in phi.table[1:]:
            pValue = float(row[-1])  # Probability
            for index in range(1, len(newTable)):  # Start from 1 to skip the header row
                #newVarValues = newTable[index][:-1]  # Variable values in the new table row
                coicidence = True
                for var in phi.scope:
                    if (row[phiIndices[var]] != newTable[index][newIndices[var]]):
                        coicidence = False
                        break
                if coicidence:
                    # Copy the probability value from self.table to newTable
                    newTable[index][-1] = float(pValue) * float(newTable[index][-1])

        return Factor(newTable)
        

    def marginalization(self, varToMarginalize):

        # Create a new table with sorted labels
        newTable = [[v for v in self.table[0] if v != varToMarginalize]]

        # Create a dictionary to map variables to their indices
        selfIndices = {var: i for i, var in enumerate(self.table[0]) if var != varToMarginalize}

        # Eliminate the variable
        for row in self.table[1:]:
            newRow = [row[selfIndices[var]] for var in self.table[0] if var != varToMarginalize]
            newTable.append(newRow)

        # Create a dictionary to store combined probabilities for similar combinations
        combinedTable = {}
        for row in newTable[1:]:
            combination = tuple(row[:-1])  # Ignore the last column (probability)
            probability = float(row[-1])  # Last column contains probability

            if combination in combinedTable:
                combinedTable[combination] += probability
            else:
                combinedTable[combination] = probability

        # Create the result table with combined combinations and summed probabilities
        resultTable = [[v for v in self.table[0] if v != varToMarginalize]]
        for combination, probability in combinedTable.items():
            resultRow = list(combination) + [probability]  # Rounded to 3 decimal places
            resultTable.append(resultRow)

        return Factor(np.array(resultTable))
    
    
    def generateCombinationTable(self, values):
        
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
    
    
    def simplifyFactor(self, variables):
        
        # Iterate over observed variables
        newTable = np.array([self.table[0]])
        selfIndices = {var: i for i, var in enumerate(newTable[0]) if var != 'p'}
        newTable = np.array([self.table[0]])

        # Remove observed variables (rows)
        for row in self.table[1:]:
            
            coincidence = False
            noneVarInTable = True
            for var in selfIndices:
                if (var in variables):
                    noneVarInTable = False
                    if (int(row[selfIndices[var]]) == variables[var]):
                        coincidence = True
                    else:
                        coincidence = False
                        break
                
                
            if coincidence or noneVarInTable:
                newTable = np.append(newTable, [row], axis=0)
                    
        # Remove unnecesary columns
        tableBody = newTable[1:]
        res = tableBody == tableBody[0,:]
        res = np.all(tableBody == tableBody[0,:], axis = 0)
        
        index = []
        for column in range(tableBody.shape[1] - 1):
            if res[column]:
                index.append(column)
        newTable = np.delete(newTable, index, 1)
    
        return Factor(newTable)
                

    def division(self, phi):
        newTable = copy.deepcopy(self.table)
        for row in newTable[1:]:
            row[-1] = float(row[-1]) / float(phi.table[1][0])
            
        return Factor(newTable)
        
        

# graph: input graph with factors as node attributes
# variable: the variable from which we want to infer the probability
# observed: dictionary (observed variable, value)
# eliminationOrder: ordered list of variables to be removed      
def variableElimination(graph, variable, observed, eliminationOrder):
    
    cantDelete = set([k for k in observed.keys()])
    cantDelete.add(variable)
    
    # Delete leaves
    graph = deleteLeaves(graph, leaves(graph), cantDelete)
    
    # Factors
    factors = []
    for v in graph.nodes:
        factors.append(graph.nodes[v]["factor"])
     
        
    # Simplification
    if len(observed) >= 1:
        simplifiedFactors = []
        for f in factors:
            newFactor = f.simplifyFactor(observed)
            if newFactor.table.shape[1] > 1:
                simplifiedFactors.append(newFactor)
        factors = simplifiedFactors

    
    # Elimination
    for v in eliminationOrder:
        if v in graph.nodes:   
            
            # Product
            newFactors = factorsWithVariable(factors, v)
            psi = newFactors[0]
            for i in range(1, len(newFactors)):
                psi = psi.product(newFactors[i])
            
            # Marginalization
            tau = psi.marginalization(v)
   
            # Update
            factors = [f for f in factors if f not in newFactors]
            factors.append(tau)
       
    
        
    # Conditional
    if observed:
        newFactors = factorsWithVariable(factors, variable)
        
        # Product
        psi = newFactors[0]
        for i in range(1, len(newFactors)):
            psi = psi.product(newFactors[i]) 
        
        # Marginalization
        tau = psi.marginalization(variable)
        
        # Division
        factors = [psi.division(tau)]  


    return factors[0]



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



# Returns the set of factors where v is in their scopes
def factorsWithVariable(factors, v):
    
    newFactors = []
    for f in factors:
        if v in f.scope:
            newFactors.append(f)
            
    return newFactors
    
    
     

