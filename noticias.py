import streamlit as st
import feedparser
from textblob import TextBlob

def exibir_noticias_analise_sentimento(selected):

    """
    Exibe notícias relacionadas a um símbolo e realiza análise de sentimento.

    Entrada:
    - selected_symbol: Símbolo selecionado.

    Saída:
    - sentiments: Lista de sentimentos das notícias.
    """
    st.subheader(f"Noticias do Time {selected}", divider='rainbow')
    # Obtenha notícias relacionadas à ação selecionada
    news_feed_sentiment = feedparser.parse(f"https://news.google.com/rss/search?q={selected.replace(' ', '%20')}&hl=pt-BR")
    news_feed_sentiment

    # Análise de Sentimento
    sentiments = []
    for entry in news_feed_sentiment.entries[:2]:
        # st.subheader(f'Noticias do Time {selected}')
        st.write(f"**Título:** {entry.title}")
        st.write(f"**Link:** [Link da Notícia]({entry.link})")
        st.write(f"**Publicado em:** {entry.published}")

    return sentiments