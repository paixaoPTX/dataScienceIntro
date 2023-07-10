#Introdução ao numpy
#Numpy Shapes

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
`

print(d)

#Devolve o número de dimensões em cada array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Podemos definir o número de dimensões do array ao criar (ndim = X)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# Podemos alterar as formas do array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape)
newarr = arr.reshape(2, 6)
print(newarr)
newarr = arr.reshape(6, 2)
print(newarr)
newarr = arr.reshape(3, 2, 2)
print(newarr)