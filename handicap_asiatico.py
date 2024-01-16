
def criar_tabela_handicap_asiatico():
    tabela = [
        [0, 'Vitória', 'Ganha'],
        [0, 'Empate', 'Devolvida'],
        [0, 'Derrota', 'Perdida'],
        [-0.25, 'Vitória', 'Ganha'],
        [-0.25, 'Empate', 'Meio Perdida'],
        [-0.25, 'Derrota', 'Perdida'],
        [0.25, 'Vitória', 'Ganha'],
        [0.25, 'Empate', 'Meio Ganha'],
        [0.25, 'Derrota', 'Perdida'],
        [-0.5, 'Vitória', 'Ganha'],
        [-0.5, 'Empate', 'Perdida'],
        [-0.5, 'Derrota', 'Perdida'],
        [0.5, 'Vitória', 'Ganha'],
        [0.5, 'Empate', 'Ganha'],
        [0.5, 'Derrota', 'Perdida'],
        [-0.75, 'Vitória por 2+', 'Ganha'],
        [-0.75, 'Vitória por 1', 'Meio Ganha'],
        [-0.75, 'Empate', 'Perdida'],
        [-0.75, 'Derrota', 'Perdida'],
        [0.75, 'Vitória', 'Ganha'],
        [0.75, 'Empate', 'Meio Perdida'],
        [0.75, 'Derrota por 1', 'Perdida'],
        [0.75, 'Derrota por 2+', 'Ganha'],
        [-1, 'Vitória por 2+', 'Ganha'],
        [-1, 'Vitória por 1', 'Meio Perdida'],
        [-1, 'Empate', 'Perdida'],
        [-1, 'Derrota', 'Perdida'],
        [1, 'Vitória', 'Ganha'],
        [1, 'Empate', 'Reembolsada'],
        [1, 'Derrota por 1', 'Perdida'],
        [1, 'Derrota por 2+', 'Ganha'],
        [-1.25, 'Vitória por 2+', 'Ganha'],
        [-1.25, 'Vitória por 1', 'Meio Perdida'],
        [-1.25, 'Empate', 'Perdida'],
        [-1.25, 'Derrota', 'Perdida'],
        [1.25, 'Vitória', 'Ganha'],
        [1.25, 'Empate', 'Meio Ganha'],
        [1.25, 'Derrota por 1', 'Perdida'],
        [1.25, 'Derrota por 2+', 'Ganha'],
        [-1.5, 'Vitória por 2+', 'Ganha'],
        [-1.5, 'Vitória por 1', 'Perdida'],
        [-1.5, 'Empate', 'Perdida'],
        [-1.5, 'Derrota', 'Perdida'],
        [1.5, 'Vitória', 'Ganha'],
        [1.5, 'Empate', 'Ganha'],
        [1.5, 'Derrota por 1', 'Perdida'],
        [1.5, 'Derrota por 2+', 'Ganha'],
        [-1.75, 'Vitória por 3+', 'Ganha'],
        [-1.75, 'Vitória por 2', 'Meio Ganha'],
        [-1.75, 'Vitória por 1', 'Meio Perdida'],
        [-1.75, 'Empate', 'Perdida'],
        [-1.75, 'Derrota', 'Perdida'],
        [1.75, 'Vitória', 'Ganha'],
        [1.75, 'Empate', 'Meio Perdida'],
        [1.75, 'Derrota por 1', 'Perdida'],
        [1.75, 'Derrota por 2+', 'Ganha'],
        [-2, 'Vitória por 3+', 'Ganha'],
        [-2, 'Vitória por 2', 'Meio Ganha'],
        [-2, 'Vitória por 1', 'Meio Perdida'],
        [-2, 'Empate', 'Perdida'],
        [-2, 'Derrota', 'Perdida'],
        [2, 'Vitória', 'Ganha'],
        [2, 'Empate', 'Reembolsada'],
        [2, 'Derrota por 1', 'Perdida'],
        [2, 'Derrota por 2+', 'Ganha'],
    ]
    return tabela


# Função para determinar o handicap do jogo


# def determinar_resultado_handicap(row, tabela_handicap):
#     colunas_m = ['M_avgP', 'M_avgG', 'M_avgSG', 'M_avgCG',
#                  'M_BTS', 'M_FTS', 'M_>1,5', 'M_>2,5', 'M_>3,5']
#     colunas_v = ['V_avgP', 'V_avgG', 'V_avgSG', 'V_avgCG',
#                  'V_BTS', 'V_FTS', 'V_>1,5', 'V_>2,5', 'V_>3,5']

#     contagem_mandante = 0
#     contagem_visitante = 0

#     for col_m, col_v in zip(colunas_m, colunas_v):
#         if row[col_m] > row[col_v]:
#             contagem_mandante += 1
#         elif row[col_m] < row[col_v]:
#             contagem_visitante += 1

#     # Se nenhum valor for maior, consideramos empate
#     if contagem_mandante == contagem_visitante:
#         return 'Empate', None
#     elif contagem_mandante > contagem_visitante:
#         handicap = 0.25  # Handicap para o mandante
#     else:
#         handicap = -0.25  # Handicap para o visitante

#     # Encontrar o resultado do handicap na tabela
#     for linha in tabela_handicap:
#         if handicap == linha[0]:
#             # Resultado correspondente encontrado na tabela
#             return linha[1], handicap

#     return None, None  # Retorna None se o resultado não for encontrado na tabela


def clean_percentage(value):
    # Trata 'n/a' como 0
    if value.lower() == 'n/a':
        return 0.0
    # Remove o caractere "%" e converte para float
    return float(value.replace('%', ''))


def determinar_resultado_handicap(row, tabela_handicap):
    colunas_m = ['M_avgP', 'M_avgG', 'M_avgSG', 'M_avgCG',
                 'M_BTS', 'M_FTS', 'M_>1,5', 'M_>2,5', 'M_>3,5']
    colunas_v = ['V_avgP', 'V_avgG', 'V_avgSG', 'V_avgCG',
                 'V_BTS', 'V_FTS', 'V_>1,5', 'V_>2,5', 'V_>3,5']

    contagem_mandante = 0
    contagem_visitante = 0

    for col_m, col_v in zip(colunas_m, colunas_v):
        valor_mandante = clean_percentage(row[col_m])
        valor_visitante = clean_percentage(row[col_v])

        if valor_mandante > valor_visitante:
            contagem_mandante += 1
        elif valor_mandante < valor_visitante:
            contagem_visitante += 1

    # Se nenhum valor for maior, consideramos empate
    if contagem_mandante == contagem_visitante:
        return 'Empate', None
    elif contagem_mandante > contagem_visitante:
        handicap = 0.25  # Handicap para o mandante
    else:
        handicap = -0.25  # Handicap para o visitante

    # Encontrar o resultado do handicap na tabela
    for linha in tabela_handicap:
        if handicap == linha[0]:
            # Resultado correspondente encontrado na tabela
            return linha[1], handicap

    return None, None  # Retorna None se o resultado não for encontrado na tabela


# # Exemplo de uso da função
# minha_tabela = criar_tabela_handicap_asiatico()

# # Iterar sobre a tabela
# for linha in minha_tabela:
#     print(linha)
