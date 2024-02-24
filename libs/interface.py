import streamlit as st
import requests
import pandas as pd
import util

import os
import json
def getAPI():
    url = 'http://localhost:8000'
    response = requests.get(url)
    print(response.json())
    return response.json()

def interface():

    # colunas presentes no dataset
    columns_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'],
    tipos = ['int', 'int', 'int', 'int', 'int', 'float', 'float', 'int']

    # titulo da aplicação
    st.title('Modelo de Machine Learning para Diabetes')
    st.write('Insira os dados do paciente para realizar a predição')

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

    # se o botão de enviar for pressionado
    if callback_enviar:
        response = requests.post('http://localhost:8000/predict/', json=data)
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write(f"Request failed with status code {response.status_code}")
    # if callback_enviar:
    #     print(data)
    #     data = json.dumps(data)
    #
    #     response = requests.post('http://localhost:8000/predict/', json=data)
        # for index, (column_name, tip) in enumerate(zip(columns,tipos)):
        #     data[column_name] = columns[index % 3].text_input(column_name + ' ('+ tip + ')', value=0)
        # response = requests.post('http://localhost:8000/predict', json=data)
        # data = {}
        # for index, (column_name, column_type) in enumerate(zip(df.columns, df.dtypes)):
        #     data[column_name] = columns[index % 3].text_input(column_name + ' ('+ str(column_type).replace('64', '') + ')', value=0)
        # response = requests.post('http://localhost:8000/predict', json=data)

        # st.write(response)
    st.write('Esta é a interface do usuário')


if __name__ == '__main__':
    # verifica se a senha de acesso está correta
    if not util.check_password():
        # se a senha estiver errada, para o processamento do app
        print("Usuario nao logado")
        st.stop()

    interface()
# interface()
