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
import dotenv
import os
import multiprocessing
import time
import subprocess

# Carregando as variáveis de ambiente
dotenv.load_dotenv()

def api_app():
    print('API Inicializada')
    os.system('cd libs && python api.py')

def interface_app():
    print('Interface Inicializada')
    os.system('cd libs && streamlit run interface.py --server.address 0.0.0.0')


if __name__ == '__main__':
    api_process = multiprocessing.Process(target=api_app)
    interface_process = multiprocessing.Process(target=interface_app)
    api_process.start()
    interface_process.start()
    # felipe andrei


