import streamlit as st
import pandas as pd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
from PIL import Image


# @st.cache
def data_load():
    data = pd.read_csv('./data/agg_prof.csv').round(2)
    return data


def home():
    st.header('Batalha de Dados')
    st.subheader('Equipe 06 - Grupos da Operação Lava Dados')
    st.subheader(""" Desafio 02: Como aprimorar o acompanhamento das competências e habilidades dos alunos de escolas estaduais a fim de reduzir uma potencial defasagem de aprendizagem em português e matemática com base na série histórica das avaliações externas?""")


def get_list_student():
    return list(data['CD_ALUNO_CRIPTO'].unique())[0:10]


def get_student(id):
    query = data['CD_ALUNO_CRIPTO'] == id
    return data.loc[query]


def plot_stundet_radar(id):

    query = data["CD_ALUNO_CRIPTO"] == id

    df = data.loc[query].copy()

    fig = px.line_polar(df, r='NOTA', theta='GRUPO',
                        line_close=True,
                        title="")
    fig.update_traces(fill='toself')

    return fig


def plot_bar(id):

    query = data["CD_ALUNO_CRIPTO"] == id

    df = data.loc[query].copy()

    fig = px.bar(df, x='NOTA', y='DESCRICAO ')

    return fig


def plt_gauge(value_prof):

    if value_prof <= 225:

        bar_col = "red"

    elif value_prof > 225 and value_prof <= 275:

        bar_col = "yellow"

    elif value_prof > 275 and value_prof <= 325:

        bar_col = "green"

    else:

        bar_col = "darkgreen"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value_prof,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [None, 500]},
               'bar': {'color': bar_col}},
        title={'text': "Proeficiência"}))

    return fig


def main():
    menu = ["Home", "Professor", "Aluno"]
    choice = st.sidebar.selectbox("Perfil", menu)

    if choice == "Home":
        st.title("BATALHA DE DADOS")
        home()

    elif choice == 'Professor':

        st.title("Perfil Professor")

        pf_menu = ["Aluno"]
        pf_choice = st.sidebar.selectbox("Professor", pf_menu)

        if pf_choice == "Aluno":

            name = random.choices(
                population=['Pedro Lima', 'Bruno Cardoso', 'José Oliveira'])[0]

            st.subheader(f"Notas do aluno (a) {name}")

            list_student = get_list_student()
            id_student = st.sidebar.selectbox(
                "Selecione o Aluno", list_student)

            st.text(f"""

                Gráfico de Radar que demonstra as Competências de português adquiridas pelo aluno específico anualmente.

                """)

            fig = plot_stundet_radar(id_student)

            st.plotly_chart(fig)

            st.text(f"""Diagrama de Proeficiências""")

            img = '/home/valeriocardoso/Documents/Projects/batalha-de-dados/app/media/materia-dependencias.png'

            image = Image.open(img)

            st.image(image, caption='Sunrise by the mountains')

            df = pd.read_csv('./data/agg_disciplinas.csv')
            st.table(df)

    elif choice == 'Aluno':

        st.title("Perfil Aluno")

        name = random.choices(
            population=['Pedro Lima', 'Bruno Cardoso', 'José Oliveira'])[0]

        st.subheader(f"Bem vindo a sua lição de Matemática {name}")

        # fig = plt_gauge(value_prof=250)

        # st.plotly_chart(fig)

        aluno_menu = ["Matemática"]
        aluno_choice = st.sidebar.selectbox("Matéria", aluno_menu)

        if aluno_choice == 'Matemática':
            st.markdown(
                "![Alt Text](https://brilliant.org/site_media/version-V87e099514e3/images/homepage/problem-solving-2x.gif)")


if __name__ == '__main__':
    data = data_load()

    main()
