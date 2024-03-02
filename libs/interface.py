import streamlit as st
import requests
import pandas as pd
import util
import dotenv

dotenv.load_dotenv()

import os
import json

cont = 0
def getAPI():
    host = os.getenv('UVICORN_URL')
    port = os.getenv('UVICORN_PORT')
    url = f'http://{host}:{port}'
    response = requests.get(url)
    print(response.json())
    return response.json()

def callback(response):
    # labels
    resposta_label = {'1': 'Diabético', '0': 'Não Diabético'}
    response = dict(response)
    st.write('Previsão: ', resposta_label[str(response['prediction'])])

def feedback():
    # feedback do usuário
    st.write("A predição está correta?")
    col1, col2, col3 = st.columns([1, 1, 5])
    with col1:
        correct_prediction = st.button('👍🏻', key='correct')
    with col2:
        wrong_prediction = st.button('👎🏻', key='wrong')

    if correct_prediction or wrong_prediction:
        st.write('Obrigado pelo feedback!')

def delsession():
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]

def interface():
    global cont
    # titulo da aplicação
    st.title('Modelo de Machine Learning para Diabetes')
    st.write('Insira os dados do paciente para realizar a predição')

    # colunas presentes no dataset
    column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                    'DiabetesPedigreeFunction', 'Age']
    tipos = ['int', 'int', 'int', 'int', 'int', 'float', 'float', 'int']

    # create the interface to insert the data
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    data = {}
    for index, (column_name, tip) in enumerate(zip(column_names, tipos)):
        data[column_name] = columns[index % 3].text_input(label=column_name, value=0, key=column_name + str(index))
    callback_enviar = st.button('Enviar')
    print('__'*30)
    for key in st.session_state.keys():
        cont += 1
        # [st.write(key, st.session_state[key]) for key in st.session_state.keys()]
        print(cont, key, st.session_state[key])
    # se o botão de enviar for pressionado
    if callback_enviar  or 'survived' in st.session_state:
        response = requests.post('http://localhost:8000/predict/', json=data)
        if response.status_code == 200:

            callback(response.json())

            feedback()

        else:
            st.write(f"Request failed with status code {response.status_code}")


        st.session_state['survived'] = 1



    st.write('Contador: ', str(cont))
    cont += 1

    # st.write('Esta é a interface do usuário')


if __name__ == '__main__':
    # verifica se a senha de acesso está correta
    if not util.check_password():
        # se a senha estiver errada, para o processamento do app
        print("Usuario nao logado")
        st.stop()

    interface()
# interface()
