import numpy as np

tempo_ms = [120, 130, 115, 140, 125, 150, 135, 110, 128, 145]

tempo_com_outlier = [
    120, 130, 115, 140, 125,
    150, 135, 110, 128, 500
]

# Python apenas para confirmar os cálculos feitos no caderno (ver questoes.md)

# Questão 8
print('======================================================================================')
print('Questão 8')

# A) Variância populacional (ddof=0 é o padrão do NumPy)
print(f'\nVariância populacional: {np.var(tempo_ms):.2f}')

# B) Desvio padrão populacional
print(f'Desvio padrão populacional: {np.std(tempo_ms):.2f}')

# Questão 9
print('======================================================================================')
print('Questão 9')

print(f'\nMédia: {np.mean(tempo_com_outlier):.1f}')
print(f'Mediana: {np.median(tempo_com_outlier):.1f}')
print(f'Amplitude: {max(tempo_com_outlier) - min(tempo_com_outlier)}')
print(f'Desvio padrão: {np.std(tempo_com_outlier):.2f}')

# Comparação com os dados sem outlier
print('\nComparação (sem outlier -> com outlier):')
print(f'Média: {np.mean(tempo_ms):.1f} -> {np.mean(tempo_com_outlier):.1f}')
print(f'Mediana: {np.median(tempo_ms):.1f} -> {np.median(tempo_com_outlier):.1f}')
print(f'Amplitude: {max(tempo_ms) - min(tempo_ms)} -> {max(tempo_com_outlier) - min(tempo_com_outlier)}')
print(f'Desvio padrão: {np.std(tempo_ms):.2f} -> {np.std(tempo_com_outlier):.2f}')