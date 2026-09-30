import pandas as pd

dados = {
    "usuario": [1,2,3,4,5,6,7,8,9,10],
    "idade": [18,22,25,31,28,35,42,24,29,33],
    "requisicoes": [10,15,8,20,12,25,18,9,14,21],
    "tempo_ms": [120,130,115,140,125,150,135,110,128,145],
    "erros": [0,1,0,2,0,3,1,0,1,2],
    "sistema": [
        "Android", "iOS", "Android", "Android", "iOS",
        "Android", "Windows", "Android", "iOS", "Android"
    ]
}

df = pd.DataFrame(dados)

# Questão 4
print('======================================================================================')
print('Questão 4')

# A) Cinco primeiras linhas
print(f'\nCinco primeiras linhas do DataFrame: \n{df.head()}')

# B) Quantidade de linhas e colunas
print(f'\nQuantidade de colunas do DataFrame: {len(df.columns)}, quantidade de linhas: {len(df)}')

# C) Informações gerais do DataFrame
print(f'\nInformações gerais: \n')
df.info()

# D) Estatísticas descritivas das variáveis numéricas
print(f'\nEstatísticas: \n{df.describe()}')
print('======================================================================================')
print('Questão 5')

# Questão 5

# A) Quantidade de usuários por sistema operacional
print('\nQuantidade de usuários por sistema operacional:\n')
print(df['sistema'].value_counts())

# B) Percentual de usuários por sistema operacional

