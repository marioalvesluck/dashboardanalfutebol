
import streamlit as st
from bardapi import Bard
import os


def ia_result(df):
    lista = list(df['Label'])

    with st.expander("Previsões da IA Prox Jogos"):
        os.environ['_BARD_API_KEY'] = "fAj2B1hbkVjk9Go5UpcpDeKOzUd7psxijqjKVd1M0PJgWl5VE9LlZs1XmzJSNORl5iTIXw."
        # st.write("""
        #         Ex de Pergunta:
        #         Crie tabela com handicap na data dos jogos de hoje com palpites de possíveis ganhadores dos jogos de futebol italiano e espanhol, qual seria melhor handicap para se jogar nos jogos e mostre análise.
        #         Crie tabela com handicap na data 2001/2024 e 21/01/2024 dos jogos de hoje com palpites de possíveis ganhadores dos jogos de futebol inglês, qual seria melhor handicap para se jogar nos jogos e mostre análise.
        #         Qual será o resultado do jogo Arsenal FC x Crystal Palace FC 2024/01/20, ganhador, qual seria o handicap ideal para este jogo e mostre análise.
        #         A classificação atual da NBA leste e oeste em formato xlsx e os próximos jogos tabela colocando a última coluna Vencedor, quem vencerá e handicap em outra coluna.
        #         """)

        times_selecionados = st.multiselect("Selecione o time: ", lista)
        if times_selecionados:
            time = ' e '.join(times_selecionados)
            # Format the question using f-string
            formatted_pergunta = f"Qual será o resultado do jogo {time}, possivel ganhador data mais recente partir de hoje, antes disso crie uma tabela da Partida e o local da Partida , posicoes dos time e porcentagem que cada time tem de ganha o jogo, crie uma tabela com handicap ideal para este jogo e mostre análise ."

            # Get the answer from the Bard model (assuming Bard class has a get_answer method)
            bard_output = Bard().get_answer(formatted_pergunta)['content']

            # Display the answer
            st.write("Resposta da IA:", bard_output)

    return df


def ia_tabela(campeonato):

    with st.expander("Tabela x Artilheiros"):
        os.environ['_BARD_API_KEY'] = "fAj2B1hbkVjk9Go5UpcpDeKOzUd7psxijqjKVd1M0PJgWl5VE9LlZs1XmzJSNORl5iTIXw."

        # # Format the question using f-string
        # formatted_pergunta = f"Crie uma tabela apresentando a classificação completa de todos os times no campeonato {campeonato} deste ano, incluindo estatísticas como jogos, vitórias, empates, derrotas, gols pró, gols contra, saldo de gols e pontos e a Porcentagem de chance de ser campeao. Além disso, gere uma tabela destacando os 10 principais artilheiros do Campeonato."

        # Format the question using f-string
        formatted_pergunta = f"Crie uma tabela apresentando a classificação completa de todos os times no campeonato {campeonato} deste ano, incluindo estatísticas como jogos, vitórias, empates, derrotas, gols pró, gols contra, saldo de gols e  pontos . Além disso, gere uma tabela destacando os 10 principais artilheiros do Campeonato."

        # Get the answer from the Bard model (assuming Bard class has a get_answer method)

        bard_output = Bard().get_answer(formatted_pergunta)['content']

        # Display the answer
        st.write("Resposta da IA:", bard_output)
    return campeonato
