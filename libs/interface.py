import streamlit as st
import requests
import pandas as pd
import os
def getAPI():
    url = 'http://localhost:8000'
    response = requests.get(url)
    print(response.json())
    return response.json()

def interface():
    df = pd.read_csv('../assets/diabetes.csv')
    df = df.drop(df.columns[-1], axis=1)

    print(df.head())
    print(df.columns)
    print(df.dtypes)

    st.title('Interface do Usuário')
    response = getAPI()

    # create the fields for the user to fill in
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    for index, (column_name, column_type) in enumerate(zip(df.columns, df.dtypes)):
        columns[index % 3].text_input(column_name + ' ('+ str(column_type).replace('64', '') + ')', value=0)
    callback_enviar = st.button('Enviar')

    st.write(response)
    st.write('Esta é a interface do usuário')
    st.write('Aqui você pode interagir com a aplicação')
# def interface():
#     df = pd.read_csv('../assets/diabetes.csv')
#
#     print(df.head())
#     print(df.columns)
#     print(df.dtypes)
#     # X = ['Gravidez', 'Glicose', 'Pressão Sanguínea', 'Espessura da Pele', 'Insulina', 'IMC', 'DiabetesPedigreeFunction',
#     #         'Idade']
#     # y = ['Outcome']
#     st.title('Interface do Usuário')
#     response = getAPI()
#
#     # criar os campos para o usuário preencher
#     for i in zip(df.columns, df.dtypes):
#         # st.write(i[0], i[1])
#         st.text_input(i[0] + ' -> '+ str(i[1]).replace('64', ''), value=0)
#     st.write(response)
#     st.write('Esta é a interface do usuário')
#     st.write('Aqui você pode interagir com a aplicação')

if __name__ == '__main__':
    interface()
# interface()
