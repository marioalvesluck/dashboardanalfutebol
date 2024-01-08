# Função para determinar o Time (Mandante ou Visitante) com base nos valores das colunas M_ e V_
def determinar_time(row):
    colunas_m = ['M_avgP', 'M_avgG', 'M_avgSG', 'M_avgCG', 'M_BTS', 'M_FTS', 'M_>1,5', 'M_>2,5', 'M_>3,5']
    colunas_v = ['V_avgP', 'V_avgG', 'V_avgSG', 'V_avgCG', 'V_BTS', 'V_FTS', 'V_>1,5', 'V_>2,5', 'V_>3,5']

    for col_m, col_v in zip(colunas_m, colunas_v):
        if row[col_m] > row[col_v]:
            return "Mandante"
        elif row[col_m] < row[col_v]:
            return "Visitante"

    # Se nenhum valor for maior, retornamos None (pode ajustar conforme necessário)
    return None


def determinar_resultado(row):
    colunas_m = ['M_avgP', 'M_avgG', 'M_avgSG', 'M_avgCG', 'M_BTS', 'M_FTS', 'M_>1,5', 'M_>2,5', 'M_>3,5']
    colunas_v = ['V_avgP', 'V_avgG', 'V_avgSG', 'V_avgCG', 'V_BTS', 'V_FTS', 'V_>1,5', 'V_>2,5', 'V_>3,5']

    contagem_mandante = 0
    contagem_visitante = 0

    for col_m, col_v in zip(colunas_m, colunas_v):
        if row[col_m] > row[col_v]:
            contagem_mandante += 1
        elif row[col_m] < row[col_v]:
            contagem_visitante += 1

    # Se nenhum valor for maior, consideramos empate
    if contagem_mandante == contagem_visitante:
        return "Empate"
    elif contagem_mandante > contagem_visitante:
        return "Mandante"
    else:
        return "Visitante"
    