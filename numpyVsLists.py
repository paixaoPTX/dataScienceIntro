#Introdução ao numpy
#Numpy vs Listas

import numpy as np

#Criação de arrays
arr = np.array([1, 2, 3, 4, 5])
lista = [1, 2, 3, 4, 5]
arr = np.array(lista)
print(type(lista))
print(type(arr))

# Operações - Slice
print(lista[2:])
print(arr[2:]) 

# Operações - Append
lista.append(6)
arr = np.append(arr, 6)
print(lista)
print(arr)

#Existem operações com comportamento diferente!
print(lista*2)
print(arr*2)