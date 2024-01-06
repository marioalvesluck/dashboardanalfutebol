import streamlit as st
from datetime import datetime
from vencedor import determinar_time
from vencedor import determinar_resultado
from funcoes_tabela import tabela_resultado, tabela_pj
from lista_times import times_al,times_esp,times_ig,times_it,times_pt,times_fr
from streamlit_autorefresh import st_autorefresh
# Título do aplicativo
st.set_page_config(page_title="Dashboard Futebol", page_icon="💹", layout="wide")

# Chamando a função resultados do Portugues
df_resultado_pt = tabela_resultado("https://native-stats.org/competition/PPL", times_pt)
# Chamando a função proximo jogos Portugues
df_pjogos_pt = tabela_pj("https://native-stats.org/competition/PPL", times_pt)
# Chamando a função  resultados italia
df_resultado_it = tabela_resultado("https://native-stats.org/competition/SA", times_it)
# Chamando a função  proximo jogos  italia
df_pjogos_it = tabela_pj("https://native-stats.org/competition/SA", times_it)

# Chamando a função  resultados copa italia
df_resultado_cit = tabela_resultado("https://native-stats.org/competition/CIT", times_it)
# Chamando a função  proximo jogos copa italia
df_pjogos_cit = tabela_pj("https://native-stats.org/competition/CIT", times_it)

# Chamando a função  resultados Espanha
df_resultado_esp = tabela_resultado("https://native-stats.org/competition/PD", times_esp)
# Chamando a função  proximo jogos Espanha
df_pjogos_esp = tabela_pj("https://native-stats.org/competition/PD", times_esp)

# Chamando a função  resultados Espanha
df_resultado_espcdr = tabela_resultado("https://native-stats.org/competition/CDR", times_esp)
# Chamando a função  proximo jogos Espanha
df_pjogos_espcdr = tabela_pj("https://native-stats.org/competition/CDR", times_esp)

# Chamando a função resultados do Inglês
df_resultado_ing = tabela_resultado("https://native-stats.org/competition/PL", times_ig)
# Chamando a função proximos jogos  do Inglês
df_pjogos_ing = tabela_pj("https://native-stats.org/competition/PL", times_ig)

# Chamando a função resultados do FAC Inglês
df_resultado_ingfac = tabela_resultado("https://native-stats.org/competition/FAC", times_ig)
# Chamando a função proximos jogos  do FAC Inglês
df_pjogos_ingfac = tabela_pj("https://native-stats.org/competition/FAC", times_ig)

# Chamando a função resultados do Alemao
df_resultado_al = tabela_resultado("https://native-stats.org/competition/BL1", times_al)
# Chamando a função proximos jogos do Alemao
df_pjogos_al = tabela_pj("https://native-stats.org/competition/BL1", times_al)

# Chamando a função resultados campeonato Frances
df_resultado_fc = tabela_resultado("https://native-stats.org/competition/FL1", times_fr)
#  Chamando a função proximos jogos campeonato Frances
df_pjogos_fc = tabela_pj("https://native-stats.org/competition/FL1", times_fr)

# # Chamando a função resultados campeonato Brasileiro
# df_resultado_br = tabela_resultado("https://native-stats.org/competition/BSA", times_br)
# #  Chamando a função proximos jogos campeonato Brasileiro
# df_pjogos_br = tabela_pj("https://native-stats.org/competition/BSA", times_br)


# Criando novas colunas para os DataFrames
def criar_novas_colunas(df):
    df[['M_avgP', 'V_avgP']] = df['avgP'].str.split(' ', expand=True)
    df[['M_avgG', 'V_avgG']] = df['avgG'].str.split(' ', expand=True)
    df['cG'] = df['cG▿']
    df[['M_avgSG', 'V_avgSG']] = df['avgSG'].str.split(' ', expand=True)
    df['cSG'] = df['cSG▿']
    df[['M_avgCG', 'V_avgCG']] = df['avgCG'].str.split(' ', expand=True)
    df[['M_BTS', 'V_BTS']] = df['BTS'].str.split(' ', expand=True)
    df[['M_FTS', 'V_FTS']] = df['FTS'].str.split(' ', expand=True)
    df[['M_>1,5', 'V_>1,5']] = df['c>1,5▿'].str.split(' ', expand=True)
    df[['M_>2,5', 'V_>2,5']] = df['c>2,5▿'].str.split(' ', expand=True)
    df[['M_>3,5', 'V_>3,5']] = df['c>3,5▿'].str.split(' ', expand=True)

    colunas_para_remover = ['avgP', 'avgG', 'cG▿', 'avgSG', 'cSG▿', 'avgCG', 'cFHG▿', 'cSHG▿', 'BTS', 'FTS', 'c>1,5▿', 'c>2,5▿', 'c>3,5▿']
    df = df.drop(columns=colunas_para_remover)

    # # df['Vencedor'] = df.apply(determinar_time, axis=1)
    df['Vencedor'] = df.apply(determinar_time, axis=1)
    # Aplicar a função ao DataFrame
    df['ResultadoFinal'] = df.apply(determinar_resultado, axis=1)

    return df

df_tabela1 = criar_novas_colunas(df_resultado_ing)
df_tabela2= criar_novas_colunas(df_pjogos_ing)
df_tabela3 = criar_novas_colunas(df_resultado_it)
df_tabela4 = criar_novas_colunas(df_pjogos_it)
df_tabela5 = criar_novas_colunas(df_resultado_esp)
df_tabela6 = criar_novas_colunas(df_pjogos_esp)
df_tabela7 = criar_novas_colunas(df_resultado_al)
df_tabela8 = criar_novas_colunas(df_pjogos_al)
df_tabela9 = criar_novas_colunas(df_resultado_pt)
df_tabela10 = criar_novas_colunas(df_pjogos_pt)

# campeonato ingles fac
df_tabela11 = criar_novas_colunas(df_resultado_ingfac)
df_tabela12= criar_novas_colunas(df_pjogos_ingfac)

# campeonato Espanhol CDR
df_tabela13 = criar_novas_colunas(df_resultado_espcdr)
df_tabela14= criar_novas_colunas(df_pjogos_espcdr)

# campeonato Frances
df_tabela15 = criar_novas_colunas(df_resultado_fc)
df_tabela16= criar_novas_colunas(df_pjogos_fc)

df_tabela17 = criar_novas_colunas(df_resultado_cit)
df_tabela18 = criar_novas_colunas(df_pjogos_cit)

tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["Campeonato Inglês", "Proximos Jogos Italiano", "Campeonato Espanhol", "Campeonato Alemão","Campeonato Portugues","Campeonato Francês"])
st_autorefresh(interval=180000, limit=100, key="fizzbuzzcounter")
with tab1:
    # Exibindo os DataFrames no Streamlit
    st.subheader("Campeonato Inglês")
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    st.subheader(f"Resultados dos jogos  Campeonato Inglês")
    st.table(df_tabela1)

    # Adicione esta linha para permitir que o usuário insira o número de acertos
    num_acertos_usuario = st.number_input("Digite o número de acertos:", min_value=0, max_value=len(df_tabela1), value=0)

    # Atualize a função contar_acertos para usar o número inserido pelo usuário
    def contar_acertos(df, num_acertos_usuario):
        df['Resultado_Correto'] = df.apply(lambda row: row['Vencedor'] if row['Vencedor'] else 'Empate', axis=1)
        acertos = num_acertos_usuario  # Use o número inserido pelo usuário
        total_jogos = len(df)
        porcentagem_acertos = (acertos / total_jogos) * 100 if total_jogos > 0 else 0
        return acertos, porcentagem_acertos

    # Atualize esta parte para mostrar os resultados usando o número inserido pelo usuário
    acertos_tabela1, porcentagem_acertos_tabela1 = contar_acertos(df_tabela1, num_acertos_usuario)

    st.write(f"Número de Acertos: {acertos_tabela1}")
    st.write(f"Porcentagem de Acertos: {porcentagem_acertos_tabela1:.2f}%")
    st.write("Contagem de Ocorrências na Coluna 'Vencedor':")
    st.write(df_tabela1['Vencedor'].value_counts())
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    st.subheader("Proximos Jogos Inglês")
    st.table(df_tabela2)
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')

    st.subheader("Resultados dos Jogos Fac Inglês")
    st.table(df_tabela11)
    
    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res_ing = df_tabela11[colunas_desejadas]
    st.dataframe(df_res_ing)

    st.subheader("Proximos Jogos FAC Inglês")
    st.table(df_tabela12)

with tab2:
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    st.subheader("Proximos Jogos Italiano")
    st.table(df_tabela4)
    st.subheader("Resultados dos jogos  Campeonato Italiano")
    st.table(df_tabela3)
        
    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela3[colunas_desejadas]
    st.dataframe(df_res)

    st.subheader("Proximos Jogos Copa da Italia")
    st.table(df_tabela18)

    st.subheader("Resultados dos jogos Copa da Italiao")
    st.table(df_tabela17)
    
    colunas_desejadas = ['Label', 'Resultado', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela18[colunas_desejadas]
    st.dataframe(df_res)

with tab3:
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    st.subheader("Proximos Jogos Campeonato Espanhol")
    st.table(df_tabela6)

    st.subheader("Resultados dos jogos Campeonato Espanhol")
    st.table(df_tabela5)

    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela5[colunas_desejadas]
    st.dataframe(df_res)

    st.subheader("Resultados dos Jogos CDR Espanhol")
    st.table(df_tabela13)

    st.subheader("Proximos Jogos CDR Espanhol")
    st.table(df_tabela14)

    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela13[colunas_desejadas]
    st.dataframe(df_res)

with tab4:
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    # Exibindo os DataFrames no Streamlit
    st.subheader("Campeonato Alemao")
    st.title(f"Proximos Jogos Alemao")
    st.table(df_tabela8)
    
    st.subheader("Resultados dos jogos Campeonato Alemao")
    st.table(df_tabela7)

with tab5:
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    # Exibindo os DataFrames no Streamlit
    st.subheader("Campeonato Portugues")
    st.title(f"Proximos Jogos Portugues")
    st.table(df_tabela10)
    
    st.subheader("Resultados dos jogos Campeonato Portugues")
    st.table(df_tabela9)

    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela9[colunas_desejadas]
    st.dataframe(df_res)

with tab6:
    st.warning('Sempre Analisar se Mandante ou Visitante esta 100% Média de Gols - Indica Possivel Ganhador')
    # Exibindo os DataFrames no Streamlit
    st.subheader("Campeonato Francês")
    st.title(f"Proximos Jogos Francês")
    st.table(df_tabela16)

    st.subheader("Resultados dos jogos Campeonato Francês")
    st.table(df_tabela15)

    colunas_desejadas = ['Label', 'Resultado', 'Status', 'Vencedor', 'ResultadoFinal']
    df_res = df_tabela15[colunas_desejadas]
    st.dataframe(df_res)