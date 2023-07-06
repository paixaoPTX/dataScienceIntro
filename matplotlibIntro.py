#Visualização com matplotlib

#Links importantes
#https://www.w3schools.com/python/matplotlib_intro.asp
#https://matplotlib.org/stable/api/index.html

import numpy as np
import matplotlib.pyplot as plt

print(np.random.normal(0, 1, size=5))
x = np.random.normal(0, 1, size=100000)
print(x)

plt.hist(x, 500)
plt.show()
plt.xlabel("Valores")


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.pie(y, labels=y)
plt.show()

plt.scatter(x, y)
plt.show()

plt.plot(np.sort(x), np.sort(y))
plt.show()