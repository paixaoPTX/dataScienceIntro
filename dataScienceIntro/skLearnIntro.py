#Introdução ao scikit-learn

#Links importantes
#https://www.w3schools.com/python/python_ml_getting_started.asp
#https://scikit-learn.org/stable/tutorial/basic/tutorial.html

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#Importar dados
df = pd.read_csv("data/carros.csv")
df.describe()

#Dividir variáveis independentes e dependente/resposta
X = df[['Weight', 'Volume']]
y = df['CO2']

X.hist()
plt.show()

y.hist()
plt.show()

#Treinar o modelo
regr = linear_model.LinearRegression().fit(X, y)


#Obter previsão
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)


#Obter interceção e coeficientes
print(regr.intercept_)
print(regr.coef_)

#y' = B0 + B1X1 + B2X2


#Exemplo de clustering
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
data
<<<<<<< HEAD
plt.scatter(x, y)
plt.show()

kmeans = KMeans(n_clusters=2)
#kmeans = KMeans(n_clusters=2, verbose=1)
=======


plt.scatter(x, y)
plt.show()

kmeans = KMeans(n_clusters=3, verbose=1)
>>>>>>> b26f580c89b951ee68b0095ef9e7344c9a9a65c7
kmeans.fit(data)

kmeans.labels_

plt.scatter(x, y, c=kmeans.labels_)
plt.show() 