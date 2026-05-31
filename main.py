# importando biblioteca
import pandas as pd

# lendo o arquivo csv, que está separado por ;
df = pd.read_csv('base_varejo.csv', sep=';')
print('Dataset carregado com sucesso.')
print('-'*50)

# exibindo principais informações do Dataset
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

print('Total de valores nulos por coluna:')
print(df.isnull().sum())
print('-'*50)

print('Total de valores duplicados:', df.duplicated().sum())
print('-'*50)

# Iniciando as 'limpezas' e copiando o Dataset para um novo
df_limpa = df.copy()

# verificando se tem valores nulos na coluna PR_CAT se tiver alterar para 'Sem Categoria'
df_limpa['PR_CAT'] = df_limpa['PR_CAT'].apply(lambda x: 'Sem Categoria' if pd.isna(x) else x)

# convertendo o tipo da coluna de data
df_limpa['DATA'] = pd.to_datetime(df_limpa['DATA'], dayfirst=True, errors='coerce')

# removendo as colunas que estão 100% vazias
df_limpa = df_limpa.dropna(axis=1, how='all')
print('Novo total de valores nulos por coluna:')
print(df_limpa.isnull().sum())
print('-'*50)

# removendo valores duplicados
df_limpa = df_limpa.drop_duplicates()
print('Novo total de valores duplicados:', df_limpa.duplicated().sum())
print('-'*50)

print('Tipos de dados de cada coluna do Dataset após conversão e limpeza:')
print(df_limpa.dtypes)
print('-'*50)

# estatisticas basicas sobre numero de filhos
print('-'*5, 'Estátisticas básicas: número de filhos', '-'*5)
print('Média:', df_limpa['CL_FHL'].mean().round(2))
print('Mediana:', df_limpa['CL_FHL'].median())
print('Desvio Padrão:', df_limpa['CL_FHL'].std().round(2))
print('Moda:', df_limpa['CL_FHL'].mode()[0])
print('Mínimo:', df_limpa['CL_FHL'].min())
print('Máximo:', df_limpa['CL_FHL'].max())
print('Contagem total:', df_limpa['CL_FHL'].count())

# calculando os quartis
q1 = df_limpa['CL_FHL'].quantile(0.25)
q2 = df_limpa['CL_FHL'].quantile(0.50)
q3 = df_limpa['CL_FHL'].quantile(0.75)

print('Q1 = (25%):', q1)
print('Q2 = (50%):', q2)
print('Q3 = (75%):', q3)
