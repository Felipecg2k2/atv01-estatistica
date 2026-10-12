# Questão 08:

# Dados (tempo_ms): 120, 130, 115, 140, 125, 150, 135, 110, 128, 145  (N = 10)

# Média = (120+130+115+140+125+150+135+110+128+145) / 10 = 1298 / 10 = 129,8 ms

# Desvios em relação à média e seus quadrados:
# 120 -> 120 - 129,8 = -9,8  -> 96,04
# 130 -> 130 - 129,8 =  0,2  -> 0,04
# 115 -> 115 - 129,8 = -14,8 -> 219,04
# 140 -> 140 - 129,8 = 10,2  -> 104,04
# 125 -> 125 - 129,8 = -4,8  -> 23,04
# 150 -> 150 - 129,8 = 20,2  -> 408,04
# 135 -> 135 - 129,8 = 5,2   -> 27,04
# 110 -> 110 - 129,8 = -19,8 -> 392,04
# 128 -> 128 - 129,8 = -1,8  -> 3,24
# 145 -> 145 - 129,8 = 15,2  -> 231,04
# Soma dos quadrados dos desvios = 1503,6

# A) Variância populacional = Σ(xi - média)² / N = 1503,6 / 10 = 150,36 ms²

# B) Desvio padrão populacional = √150,36 ≈ 12,26 ms

# O desvio padrão de aproximadamente 12,26 ms indica que, em média, os tempos de resposta se afastam cerca de 12,26 ms da média (129,8 ms).
# Ou seja, a maior parte dos tempos fica entre aproximadamente 117,5 ms e 142,1 ms. Como o valor é pequeno em relação à média (cerca de 9,4%), os tempos têm pouca variação.

# Questão 09:

# Dados (tempo_com_outlier): 120, 130, 115, 140, 125, 150, 135, 110, 128, 500

# Média = (120+130+115+140+125+150+135+110+128+500) / 10 = 1653 / 10 = 165,3 ms

# Mediana: ordenando -> 110, 115, 120, 125, 128, 130, 135, 140, 150, 500
# Como N = 10 (par), a mediana é a média dos dois valores centrais: (128 + 130) / 2 = 129 ms

# Amplitude = máximo - mínimo = 500 - 110 = 390 ms

# Desvios em relação à média (165,3) e seus quadrados:
# 120 -> -45,3 -> 2052,09
# 130 -> -35,3 -> 1246,09
# 115 -> -50,3 -> 2530,09
# 140 -> -25,3 -> 640,09
# 125 -> -40,3 -> 1624,09
# 150 -> -15,3 -> 234,09
# 135 -> -30,3 -> 918,09
# 110 -> -55,3 -> 3058,09
# 128 -> -37,3 -> 1391,29
# 500 -> 334,7 -> 112024,09
# Soma dos quadrados dos desvios = 125718,1

# Variância populacional = 125718,1 / 10 = 12571,81 ms²
# Desvio padrão populacional = √12571,81 ≈ 112,12 ms

# Comparação com os resultados anteriores:
# Média:         129,8 ms -> 165,3 ms  (aumentou 35,5 ms)
# Mediana:       129 ms   -> 129 ms    (não mudou)
# Amplitude:     40 ms    -> 390 ms    (quase 10 vezes maior)
# Desvio padrão: 12,26 ms -> 112,12 ms (cerca de 9 vezes maior)

# Questão 10:

# O valor 500 ms é um outlier (valor extremo), muito distante dos demais (que ficam entre 110 e 150 ms).
# A média e o desvio padrão utilizam todos os valores no cálculo (e o desvio padrão ainda eleva as distâncias ao quadrado), então um único valor muito grande puxa a média para cima e faz o desvio padrão explodir.
# A amplitude depende apenas do máximo e do mínimo, e o outlier passa a ser o máximo.
# Já a mediana depende apenas da posição dos valores centrais, por isso não foi alterada.

# Neste caso a mediana representa melhor o comportamento típico dos tempos. Ela continua em 129 ms, valor que condiz com quase todas as requisições.
# A média (165,3 ms) ficou maior do que 9 dos 10 tempos, ou seja, não representa nenhuma requisição típica, pois foi distorcida por um único valor.