#Introdução ao Numpy
#Operações em Numpy

#Links importantes:
#https://numpy.org/doc/stable/reference/index.html	
#https://www.w3schools.com/python/numpy/default.asp


import numpy as np

#Operações básicas
a = np.array([1, 2, 3, 4])
print(a+2)
print(a*5)
print(a**2)


#Operações entre arrays
b = np.array([42, 5, 4, 5])
print(np.inner(a, b))
print(np.outer(a, b))
print(np.multiply(a, b))

#Obter Sets
print(np.unique(b))

#Mínimo Múltiplo Comum
print(np.lcm(4, 6))
print(np.lcm.reduce(a))


#Operações em Matrizes
#Existe mesmo a class Matrix no Numpy
#https://numpy.org/doc/stable/reference/routines.matlib.html#

newarr = a.reshape(2, 2)
print(newarr)

print(np.linalg.inv(newarr))
print(np.linalg.det(newarr))
print(np.linalg.eigvals(newarr))
print(np.linalg.eig(newarr))

#Funções Random

x = np.random.poisson(lam=2, size=10)
print(x)