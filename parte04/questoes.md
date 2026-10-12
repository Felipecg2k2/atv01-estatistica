# Questão 11:

# Probabilidade experimental = (casos favoráveis) / (total de casos)
# Requisição com erro: erros > 0

# Erros: 0, 1, 0, 2, 0, 3, 1, 0, 1, 2

# Quantidade total de requisições = 10
# Quantidade de requisições com erro = 6 (usuários 2, 4, 6, 7, 9 e 10)
# Probabilidade P(A) = 6 / 10 = 0,6
# Porcentagem = 60%

# Questão 12:

# P(Ac) = 1 - P(A)
# P(Ac) = 1 - 0,6 = 0,4
# A probabilidade de uma requisição não apresentar erro é de 0,4 (40%).

# Questão 13:

# Sistemas: Android = 6, iOS = 3, Windows = 1 (total = 10)

# A) P(Android) = 6 / 10 = 0,6 (60%)

# B) P(iOS) = 3 / 10 = 0,3 (30%)

# C) P(não Android) = 1 - P(Android) = 1 - 0,6 = 0,4 (40%)
# Conferindo: (3 iOS + 1 Windows) / 10 = 4 / 10 = 0,4

# Questão 14:

# Números primos em um dado de 6 faces: 2, 3 e 5.
# Probabilidade teórica = 3 / 6 = 0,5 (50%)

# A probabilidade experimental (simulação com 10.000 lançamentos) está em ex.py e fica muito próxima de 0,5.
# Os valores podem ser ligeiramente diferentes porque a simulação depende do acaso: com um número finito de lançamentos,
# a frequência observada varia em torno da probabilidade teórica. Quanto maior o número de lançamentos, mais o resultado
# se aproxima do valor teórico (Lei dos Grandes Números).

# Questão 15:

# Com base nos dados analisados, como podemos descrever o comportamento do sistema?

# O desempenho do sistema é estável. O tempo de resposta médio é de 129,8 ms e a mediana é de 129 ms, valores muito próximos,
# o que indica uma distribuição simétrica. O desvio padrão é baixo (12,26 ms, cerca de 9% da média) e a amplitude é de
# apenas 40 ms (entre 110 e 150 ms), então os tempos variam pouco e não há valores extremos (outliers).
# Em relação ao perfil dos usuários, o Android domina com 60%, seguido por iOS (30%) e Windows (10%).
# Já a confiabilidade é um ponto de atenção: a probabilidade estimada de uma requisição apresentar erro é de 60%,
# ou seja, 6 das 10 requisições registraram ao menos um erro, uma taxa alta.
# Conclusão: o sistema é rápido e consistente, mas tem uma taxa de erros elevada que deve ser investigada pela equipe.
# Obs.: a amostra tem apenas 10 registros, então as conclusões são indicativas e não devem ser generalizadas sem mais dados.