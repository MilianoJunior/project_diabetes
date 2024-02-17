'''
Descrição: Modelo preditivo do dataset de diabetes
Autor: Miliano F. de Oliveira Junior
       Álvaro Pagliari

Disciplina: Implantação de Modelos de Machine Learning
Professor: Dr. Felipe de Morais

Requisitos:

    Utilizar o dataset de Diabetes (visto em outra disciplina do curso)
    Selecionar um modelo treinado e validado
    Desenvolver uma aplicação utilizando Streamlit que permita o usuário entrar com os dados
    Realizar a predição/aplicação do modelo treinado e retornar o resultado para o usuário
    Capturar o feedback do usuário para poder avaliar a solução
    Calcular métricas de avaliação e exibir os resultados na tela
    Subir o código para um repositório Git
    Realizar a implantação da solução na AWS – EC2

Estrutura do projeto:

    - diabetes-predictor/
        - main.py: Código principal da aplicação.
        - requirements.txt: Lista de dependências do projeto.
        - .env: Variáveis de ambiente.
        - README.md: Descrição e instruções do projeto.
        - .gitignore: Arquivos e pastas ignorados pelo Git.
        - LICENSE: Licença de uso do projeto.
        - libs/: Bibliotecas desenvolvidas para o projeto, incluindo:
          - api.py: Implementação da API.
          - interface.py: Interface do usuário.
          - login.py: Autenticação de usuário.
        - assets/: Arquivos estáticos (imagens, CSS, JS).
        - data/: Dados utilizados pelo projeto.

'''

# Importando as bibliotecas
from libs import api, interface, login
import dotenv
import os
import multiprocessing
import time

# Carregando as variáveis de ambiente
dotenv.load_dotenv()



# Inicializando a aplicação
def api_app():
    # api.app.run(debug=True, port=8080, host='
    print('API Inicializada')
    cont = 0
    while True:
        print(cont, 'API Rodando')
        time.sleep(1)
        cont += 1
        if cont > 10:
            break
    return True

def interface_app():

    print('Interface Inicializada')
    cont = 0
    while True:
        print(cont, 'Interface Rodando')
        time.sleep(1)
        cont += 1
        if cont > 10:
            break
    return True

if __name__ == '__main__':

    # Ultilizar o multiprocessing para inicializar a API e a interface do usuário
    # Inicializando a API
    api_process = multiprocessing.Process(target=api_app)
    api_process.start()

    # Inicializando a interface do usuário
    interface_process = multiprocessing.Process(target=interface_app)
    interface_process.start()

