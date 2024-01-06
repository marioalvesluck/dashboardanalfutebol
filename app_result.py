from funcoes_tabela import tabela_resultado, tabela_pj
from lista_times import times_al,times_esp,times_ig,times_it,times_pt,times_fr

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

# Chamando a função resultados campeonato Frances
df_resultado_br = tabela_resultado("https://native-stats.org/competition/BSA", times_fr)
#  Chamando a função proximos jogos campeonato Frances
df_pjogos_br = tabela_pj("https://native-stats.org/competition/BSA", times_fr)