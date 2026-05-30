import pandas as pd

df = pd.read_csv('base_varejo.csv', sep=';')
print('Dataset carregado com sucesso.')
print('-'*50)

print('Número de linhas e colunas do Dataset:', df.shape)
print('-'*50)

print('Tipos de dados de cada coluna do Dataset:')
print(df.dtypes)
print('-'*50)

print('Nome das coluna do Dataset:')
print(df.columns)
print('-'*50)

print('Primeiras linhas do Dataset:')
print(df.head(10))
print('-'*50)
