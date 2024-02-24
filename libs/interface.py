import streamlit as st
import requests

def getAPI():
    url = 'http://localhost:8000'
    response = requests.get(url)
    print(response.json())
    return response.json()
def interface():
    st.title('Interface do Usuário')
    response = getAPI()
    st.write(response)
    st.write('Esta é a interface do usuário')
    st.write('Aqui você pode interagir com a aplicação')

if __name__ == '__main__':
    interface()
# interface()
