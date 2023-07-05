#Introdução ao Pandas

#Links importantes
#www.w3schools.com/python/pandas/default.asp
#https://pandas.pydata.org/docs/

import pandas as pd
import matplotlib.pyplot as plt

#Importar datasets
df = pd.read_csv('dataScienceIntro/data.csv')
print(df)
print(df.to_string())

print(df.head(10))
print(df.tail())

#Exportar e importar ficheiros excel (index=False -> não exporta o index para o ficheiro excel)
#df.to_excel('dataScienceIntro/data.xlsx')
df.to_excel('dataScienceIntro/data.xlsx', index=False)
df=pd.read_excel('dataScienceIntro/data.xlsx')

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
