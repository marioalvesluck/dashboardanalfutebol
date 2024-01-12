import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def class_times(classificacao):
    # Criar o gráfico de barras verticais com valores
    teams = list(classificacao['Name'][:10])
    scores = list(classificacao['P'][:10])

    # Ajuste o tamanho da figura conforme necessário
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(teams, scores)

    # Adicionar os valores acima das barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval,
                round(yval, 1), ha='center', va='bottom')

    # Configurar título e rótulos dos eixos
    ax.set_title('Classificação das Equipes')
    ax.set_xlabel('Equipes')
    ax.set_ylabel('Pontuações')

    # Inclinar as etiquetas no eixo x para evitar sobreposição
    plt.xticks(rotation=45, ha='right')

    # Retornar a figura (em vez de exibi-la)
    return fig
