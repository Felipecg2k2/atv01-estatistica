import pandas as pd
import matplotlib.pyplot as plt

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

# Questão 15
print('======================================================================================')
print('Questão 15')

# A) Estatística descritiva
tempo = df['tempo_ms']

print('\nA) Estatística descritiva do tempo de resposta:\n')
print(f'Média: {tempo.mean():.1f} ms')
print(f'Mediana: {tempo.median():.1f} ms')
print(f'Amplitude: {tempo.max() - tempo.min()} ms')
print(f'Desvio padrão (populacional): {tempo.std(ddof=0):.2f} ms')

# B) Análise de frequência
print('\nB) Distribuição dos usuários por sistema operacional:\n')
frequencia = df['sistema'].value_counts()
percentual = df['sistema'].value_counts(normalize=True) * 100
print(pd.DataFrame({'quantidade': frequencia, 'percentual (%)': percentual}))

# C) Probabilidade
prob_erro = (df['erros'] > 0).mean()
print(f'\nC) Probabilidade estimada de uma requisição apresentar erro: {prob_erro:.1f} ({prob_erro * 100:.0f}%)')

# D) Visualização
# Gráfico 1: distribuição dos sistemas operacionais
plt.figure(figsize=(7, 5))
plt.bar(frequencia.index, frequencia.values)
plt.title('Distribuição dos sistemas operacionais')
plt.xlabel('Sistema operacional')
plt.ylabel('Quantidade de usuários')
plt.show()

# Gráfico 2: distribuição dos tempos de resposta
faixas = [105, 115, 125, 135, 145, 155]
plt.hist(tempo, bins=faixas, color='skyblue', edgecolor='black')
plt.xticks(faixas)
plt.title('Distribuição dos tempos de resposta')
plt.xlabel('Tempo de resposta (ms)')
plt.ylabel('Frequência')
plt.show()

# E) Interpretação
print('\nE) Interpretação:\n')
print(f'O tempo de resposta do sistema é estável: a média (129,8 ms) e a mediana (129 ms) são muito próximas,')
print(f'o desvio padrão é baixo (12,26 ms, cerca de 9% da média) e a amplitude é de apenas 40 ms (110 a 150 ms),')
print(f'sem valores extremos. A base de usuários é concentrada no Android (60%), seguido de iOS (30%) e Windows (10%).')
print(f'Por outro lado, a probabilidade estimada de erro é alta (60%): 6 das 10 requisições registraram erro.')
print(f'Portanto, o sistema é estável quanto ao desempenho, mas apresenta um ponto de atenção na confiabilidade.')