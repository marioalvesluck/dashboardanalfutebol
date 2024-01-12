import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import streamlit as st
@st.cache_data
def tabela_resultado(url, nomes_substituir):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar a tabela
        table = soup.find('table', {'class': 'min-w-full divide-y divide-gray-300'})

        # Extrair dados da tabela usando Pandas
        df = pd.read_html(StringIO(str(table)))[0]
        df = df.rename(columns={'Unnamed: 1': 'Resultado', 'Unnamed: 2': 'Status'})

        # Filtrar a coluna 'Label' para manter apenas os nomes presentes em nomes_substituir
        df['Label'] = df['Label'].apply(lambda x: ' x '.join([nome for nome in nomes_substituir if nome in x]))
      
        return df
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        return None
    
@st.cache_data
def tabela_pj(url, nomes_substituir):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', {'class': 'min-w-full divide-y divide-gray-300'})

        if len(tables) >= 2:
            segunda_tabela = tables[1]
            df = pd.read_html(StringIO(str(segunda_tabela)))[0]
            df = df.rename(columns={'Unnamed: 1': 'Resultado', 'Unnamed: 2': 'Horario'})
            
            # Filtrar a coluna 'Label' para manter apenas os nomes presentes em nomes_substituir
            df['Label'] = df['Label'].apply(lambda x: ' x '.join([nome for nome in nomes_substituir if nome in x]))
            
            if 'Horario' in df.columns:
                if df['Horario'].str.contains(',').all():
                    try:
                        df['Horario'] = df['Horario'].str.replace(', ', ',')
                        df[['Data', 'Horario']] = df['Horario'].str.split(',', expand=True).iloc[:, :2]
                    except ValueError as e:
                        print(f"Erro ao dividir 'Horario': {e}")
                else:
                    print("Alguns valores na coluna 'Horario' não contêm uma vírgula.")
            else:
                print("A coluna 'Horario' não está presente no DataFrame.")

            return df
        else:
            st.warning("Menos de duas tabelas encontradas.")
            return None
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        return None
    
@st.cache_data
def tabela_class(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar a tabela
        table = soup.find('table', {'class': 'w-full divide-y divide-gray-300 mb-6 leading-none'})

        # Extrair dados da tabela usando Pandas
        df = pd.read_html(StringIO(str(table)))[0]

        return df
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        return None
    
@st.cache_data
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