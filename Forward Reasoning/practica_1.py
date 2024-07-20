# -*- coding: utf-8 -*-'

# =============================================================================
#
#     Representación del Conocimiento
#         Práctica 1
#             Encadenamiento hacia delante en logica proposicional
#         
#     - Arahi Fernandez Monagas
#     - Iker Martinez Gomez
#     - Carlos Velazquez Fernandez
# 
# =============================================================================


import copy
import re
import numpy as np


# Reglas: conjunto de reglas (antecedente -> consecuente)
# Hechos: conjunto de proposiciones
# Aplica encadenamiento hacia delante para ampliar la base de conocimiento
def encadenamiento(reglas, hechos):
    modificacion = True
    reglasDisparadas = set()
    
    # Acabamos cuando se recorran las reglas sin hacer modificaciones
    while modificacion:
        modificacion = False 
        
        # Recorremos las reglas
        for regla in reglas:
            
            # Si ya la hemos disparado no se puede volver a usar
            if regla not in reglasDisparadas:
                antecedente = compruebaFnc(regla[0])
                    
                # Comprobamos si tenemos todos los antecedentes en la BC
                # En caso afirmativo, si no esta ya el consecuente en la BC, lo anhadimos
                if all(hecho in hechos for hecho in antecedente):
                    consecuente = compruebaFnc(regla[1])
                    
                    for c in consecuente:
                        hechos.add(c)
                        
                    reglasDisparadas.add(regla)
                    modificacion = True
            

    # Resultado final = reglas + hechos
    bc = reglas.union(hechos)
    return setToString(bc)



# expr: Una proposicion cualquiera
# Retorna una lista con expresiones si expr es una FNC
# o una lista de la forma [expr] en caso contrario
def compruebaFnc(expr):
    # Si es una FNC, separamos los elementos
    if expr.find('v') == -1:
        expr = expr.split("^")
        expr = [('(' + e + ')') for e in expr if not '(' in expr]
    
    # Si no es una FNC, los comprobamos como conjunto
    else:
        expr = ['(' + str(expr) + ')']

    return expr



# bc: base de conocmienton (string)
# Retorna dos conjuntos:
#   reglas: (antecedente -> consecuente)
#   hechos: proposicion
def stringToSet(bc):
    
    # Elimina espacios
    string = re.sub(r' +', '', bc)
    
    # Separa expresiones
    p = 0
    p_copia = 0
    level = 0
    copia = copy.deepcopy(string)
    for char in string:
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
        else:
            if level == 0 and char == '^':
                copia = copia[:p_copia] + 'AND' + copia[p_copia+1:]
                p_copia += 2

        p += 1
        p_copia += 1
        
    # Separa reglas de hechos
    string = copia.split("AND")
    reglas = set()
    hechos = set()
    for elemento in string:
        s1 = elemento.replace("(", "")
        s2 = s1.replace(")","")
        if '->' in elemento:
            s1 = elemento.replace("(","")
            s2 = s1.replace(")","")
            s3 = s2.split("->")
            reglas.add((s3[0], s3[1]))
        else:
            hechos.add('(' + s2 + ')')
    
    return reglas, hechos
    

# bc: base de conocimiento en forma de conjunto
# Retorna la misma bc formateada como string
def setToString(bc):
    string = ""
    first = True
    for proposicion in bc:
        proposicion = str(proposicion).replace('^', ' ^ ')
        if first:
            string += str(proposicion)
            first = False
        else:
            string += " ^ " + proposicion
    string = string.replace(',', ' ->')
    string = string.replace('\'', '')
    string = string.replace('v', ' v ')
    return string


# Retorna True si el encadanemiento es completo;
# False en caso contrario
def esCompleto(bc):

    # Encuentra todas las variables
    variables = set(re.findall("[A-Z]+", bc))
    nVariables = len(variables)
    nRows = 2**nVariables
    table = np.zeros((nRows, nVariables), dtype=int)
    
    # Crea tabla de verdad
    for i in range(nRows):
        binary = bin(i)[2:]
        j = nVariables - 1 
        for value in reversed(binary):
            table[i][j] = value
            j -= 1

    
    # Orden de las variables
    index = {}
    i = 0
    for v in variables:
        index[v] = i
        i += 1
        
    # Calcula el valor de verdad de la base de conocimiento
    bcValues = []
    substitution = replaceImplication(bc)
    substitution = substitution.replace('^', '&')
    substitution = substitution.replace('v', '|')
    substitution = replaceNot(substitution)
    
    for row in table:
        combination = copy.deepcopy(substitution)
        for variable in variables:
            combination = combination.replace(str(variable), str(row[index[variable]]))
        value = eval(combination)
        bcValues.append(value)
        
    table = np.c_[table, bcValues]   
    
    # Derivaciones semanticas
    derivacionesSemanticas = set()
    tablaDerivaciones = np.ones((nRows, nVariables+1), dtype=int)
    for i in range(len(table)):
        if table[i][-1] == 1:
            tablaDerivaciones[i] = table[i]
            
    derivaciones = np.ones((1, nVariables+1), dtype=int)
    for row in tablaDerivaciones:
        derivaciones = derivaciones & row
    
    for i in range(nVariables):
        if derivaciones[0][i] == 1:
            v = [j for j in index if index[j]==i]
            derivacionesSemanticas.add('(' + v[0] + ')')
    
    # Derivaciones sintacticas
    _, hechos = stringToSet(bc)
    # Comprobacion de completitud
    if derivacionesSemanticas.issubset(hechos):
        completo = True
    else:
        completo = False
        
    return completo


# Reemplaza las implicaciones de un string de la siguiente forma :
# p -> q    <=========>    (p ^ q) v ~p   
def replaceImplication(string):

    while '-' in string:
        newString = ""
        level = 0
        i = 0
        
        while i < len(string):
            c = string[i]
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            elif c == '-':
                left = ""
                right = ""
    
                # Left
                sublevel = 0
                for j in range (i, -1, -1):
                    if string[j] == ')':
                        sublevel += 1
                    elif string[j] == '(':
                        sublevel -= 1
                        if sublevel == -1:
                            left = string[j+1:i]
                            break
                
                # Right
                sublevel = 0
                for k in range (i+2, len(string), 1):
                    if string[k] == '(':
                        sublevel += 1
                    elif string[k] == ')':
                        sublevel -= 1
                        if sublevel == -1:
                            right = string[i+2:k]  
                            break
                
                implication = '(((' + left + ') ^ (' + right + ')) v ~(' + left + '))'
                newString = string[:j] + implication + string[k+1:]
                string = copy.deepcopy(newString)
                i = (k-i) + len(implication)
            
            i += 1
       
    return string
     

# Reemplaza las negaciones en un string de la siguiente forma:
#  ~p   <=========>   (not p)   
def replaceNot(string):
    
    newString = ""
    counter = 0
    index = 0
    for c in string:
        if counter > 0:
            counter -= 1
        elif c == '~':
            s, counter = createNot(string[index+1:])
            newString += s
        else:
            newString += c
        index += 1

    return newString

# Funcion auxiliar de replaceNot
def createNot(string):
    newString = '(not '
    index = 0
    level = 0
    counter = 0
    expr = False
    for c in string:
        if counter > 0:
            counter -= 1
        else:
            if c == '~':
                s, counter = createNot(string[index+1:])
                newString += s
            elif c == '(':
                level += 1
                expr = True
            elif c == ')':
                level -= 1
                if level <= 0:
                    newString += ')'
                    return newString, index
            elif c == ' ' and not expr:
                newString += ')'
                return newString, index
            if counter == 0:
                newString += c
        index += 1
        
    
    newString += ')'
    return newString, index
    

