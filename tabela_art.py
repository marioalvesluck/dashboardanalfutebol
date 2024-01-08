import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import streamlit as st

def tabela_art(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', {'class': 'w-full divide-y divide-gray-300 mb-6 leading-none'})

        if len(tables) >= 2:
            segunda_tabela = tables[1]
            df = pd.read_html(StringIO(str(segunda_tabela)))[0]
            df = df.rename(columns={'Unnamed: 1': 'Resultado', 'Unnamed: 2': 'Horario'})

            # Remover parte duplicada do nome após o segundo espaço vazio
            df['Name'] = df['Name'].apply(lambda x: x.split('  ')[0])

            return df
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        return None
    
print(tabela_art('https://native-stats.org/competition/PL'))