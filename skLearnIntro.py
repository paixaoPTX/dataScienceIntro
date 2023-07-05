#Introdução ao scikit-learn

#Links importantes
#https://www.w3schools.com/python/python_ml_getting_started.asp
#https://scikit-learn.org/stable/tutorial/basic/tutorial.html

import pandas as pd
from sklearn import linear_model

#Importar dados
df = pd.read_csv("dataScienceIntro/carrosW.csv")
df.describe()

#Dividir variáveis independentes e dependente/resposta
X = df[['Weight', 'Volume']]
y = df['CO2']

#Treinar o modelo
regr = linear_model.LinearRegression()
regr.fit(X, y)

#Obter previsão
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)

#Obter interceção e coeficientes
print(regr.intercept_)
print(regr.coef_)


#Exemplo de clustering
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data = list(zip(x, y))
plt.scatter(x, y)
plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show() 