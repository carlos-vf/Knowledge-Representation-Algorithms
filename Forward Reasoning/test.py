# -*- coding: utf-8 -*-
'''
    Representacion del Conocimiento
        TESTS Practica 1
            Encadenamiento hacia delante en logica proposicional
        
    - Arahi Fernandez Monagas
    - Iker Martinez Gomez
    - Carlos Velazquez Fernandez
'''

import practica_1 as p1

print("Test funcionamiento algoritmo Encadenamiento\n")

#Reglas: CH 
#Hechos: no CH
print("Caso 1")
x = "(A ^ B -> C) ^ (C -> D) ^ (E -> A ^ F) ^ E ^ F ^ A ^ B"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en el primer caso es completo."
print()

#Reglas: no CH 
#Hechos: no CH
print("Caso 2")
x = "(A ^ B -> C) ^ (C -> D) ^ (E -> ~F v A) ^ G ^ ~H"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

#Reglas: no CH 
#Hechos: no CH
print("Caso 3")
x = "(A -> ~B v C) ^ (D -> E) ^ (F ^ G -> ~H ^ I) ^ J ^ ~K ^ L ^ A ^ ~B"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

#Reglas: no CH 
#Hechos: no CH
print("Caso 4")
x = "(~X -> Y ^ ~Z) ^ (W -> V) ^ (U ^ T -> ~S ^ R) ^ Q ^ P ^ O ^ ~A ^ B"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

#Reglas: CH 
#Hechos: CH
print("Caso 5")
x = "(A -> B) ^ (C -> D) ^ (E -> A ^ F) ^ E ^ F ^ G ^ H"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

#Reglas: no CH 
#Hechos: no CH
print("Caso 6")
x = "(A ^ B -> C) ^ (C -> D) ^ (E -> ~F v A) ^ G ^ ~H ^ A"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: no CH
# Hehos: no Ch
print("Caso 7")
x = "(~X -> Y ^ ~Z) ^ (W -> V) ^ (U ^ T -> ~S ^ R) ^ Q ^ P ^ O ^ ~X ^ B ^ ~W"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: CH
# Hehos: CH
print("Caso 8")
x = "(A -> B) ^ (B -> C) ^ (C -> D) ^ (D -> A) ^ A ^ D"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: CH
# Hehos: CH
print("Caso 9")
x = "(A ^ B -> C) ^ (C -> D) ^ (E -> A ^ F) ^ A ^ B ^ C ^ D ^ E"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: CH
# Hechos: CH
print("Caso 10")
x = "(A -> B) ^ (B -> C) ^ (C -> D) ^ A ^ B ^ C ^ D"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: CH
# Hechos: CH
print("Caso 11")
x = "(P ^ Q -> R) ^ (R -> S) ^ (S -> T) ^ P ^ Q ^ R ^ S ^ T"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert completo, "El encadenamiento en este caso debería ser completo."
print()

# Reglas: no CH
# Hehos: no CH
print("Caso 12")
x = "(A v B -> C) ^ (A v C)"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert not completo, "El encadenamiento en este caso debería no ser completo."
print()

# Reglas: CH
# Hehos: no CH
print("Caso 13")
x=  "(L -> M) ^ (L v M)"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert not completo, "El encadenamiento en este caso debería no ser completo."
print()

# Reglas: no CH
# Hehos: CH
print("Caso 14")
x =   "(L v N -> M) ^ L"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert not completo, "El encadenamiento en este caso debería no ser completo."
print()

# Reglas: no CH
# Hehos: CH
print("Caso 15")
x= "(A ^ C -> E) ^ (B -> C) ^ (B v D -> F) ^ (C -> D) ^ B"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert not completo, "El encadenamiento en este caso debería no ser completo."
print()

# Reglas: no CH
# Hehos: CH
print("Caso 16")
x= "(A v B -> C) ^ A ^ B"
reglas, hechos = p1.stringToSet(x)
enc = p1.encadenamiento(reglas, hechos)
completo = p1.esCompleto(enc)
print("Encadenamiento: ", enc)
print("Completo: ", completo)
assert not completo, "El encadenamiento en este caso debería no ser completo."
print()

print("Todos los casos de prueba han pasado.")
