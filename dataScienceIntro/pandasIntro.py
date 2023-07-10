#Introdução ao Pandas

#Links importantes
#www.w3schools.com/python/pandas/default.asp
#https://pandas.pydata.org/docs/

import pandas as pd
import matplotlib.pyplot as plt

#Importar datasets
df = pd.read_csv('data.csv')
print(type(df))
print(df)
print(df.to_string())

print(df.head(10))
print(df.tail())

#Exportar e importar ficheiros excel (index=False -> não exporta o index para o ficheiro excel)
#df.to_excel('data.xlsx')
df.to_excel('data.xlsx', index=False)
df=pd.read_excel('data.xlsx')

#Informação e Estatistica do DF
print(df.info()) 
print(df.describe())

# Acesso à linha
print(df.loc[0])

########

# Obter nova DF sem valores vazios
print(len(df))
df.dropna()
print(len(df))
new_df = df.dropna()
print(len(new_df))

#Substituir valores vazios por valor mediano da coluna Calories
print(df.loc[91])
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True) 
print(df.loc[91])

#Plotting com Pandas

df.plot()
plt.show()

df.plot(subplots=True, sharex=True, sharey=False, figsize=(32, 60), fontsize=32)
[ax.legend(loc = 2, fontsize =  10) for ax in plt.gcf().axes]
plt.show()

df["Calories"].plot(kind='hist')
plt.show()

df.hist()
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()


#Coorelação
print(df.corr())
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

#Visualização da Coorelação
import seaborn as sb


corr = df.corr()
sb.heatmap(corr, cmap="Blues", annot=True)
plt.show()

#Mais operações com a biblioteca pandas

df.transpose()

df = pd.DataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
other = pd.DataFrame([[0, 1], [1, 2], [-1, -1], [2, 0]])
df.dot(other)

alunos = pd.DataFrame([["António", 1112], ["José", 1112], ["Sofia", 1112], ["Sofia", 1113], ["Sofia", 1114]], columns=["aluno", "codigoUC"])
ucs = pd.DataFrame([[1111, "Java"], [1112, "Python"], [1113, "Python Avançado"]], columns=["codigoUC", "nomeUC"])
pd.merge(alunos, ucs, on  = ["codigoUC"], how="inner")

#Exemplo Pivot Tables
import numpy as np

data = {'Category': ['A', 'A', 'B', 'B', 'A', 'B'], 
        'Year': ['2019', '2019', '2020', '2020', '2021', '2021'], 
        'Quantity': [10, 15, 20, 5, 12, 8], 
        'Price': [100, 150, 200, 50, 120, 80]}

df = pd.DataFrame(data)
pivot_sum = pd.pivot_table(df, values='Quantity', index='Category', columns='Year', aggfunc=np.sum)
print(pivot_sum)
pivot_count = pd.pivot_table(df, values='Quantity', index='Category', columns='Year', aggfunc='count')
print(pivot_count)
pivot_mean = pd.pivot_table(df, values='Quantity', index='Category', columns='Year', aggfunc=np.mean)
print(pivot_mean)
pivot = pd.pivot_table(df, values='Quantity', index='Category', columns='Year',
                             aggfunc=['count', np.sum])
print(pivot)