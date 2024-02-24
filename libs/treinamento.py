import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import streamlit as st
import os

print(os.getcwd())
# Carregando os dados
df = pd.read_csv('assets/diabetes.csv')

print(df.head())
print(df.columns)
# Análise básica: df.describe(), df.info()

# Limpeza dos dados: preencher ou remover valores faltantes
# df.fillna(metodo_de_preenchimento) ou df.dropna()

# Definir as variáveis independentes (X) e a variável dependente (y)
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['Outcome']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalização dos dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
    'penalty': ['l2'],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
}

# Initialize the GridSearchCV
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='accuracy')

# Fit the model
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters
best_params = grid_search.best_params_

# Train the model with the best parameters
model = LogisticRegression(**best_params)
model.fit(X_train_scaled, y_train)

# Evaluate the model
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia: {accuracy}')

# salvar o modelo
joblib.dump(model, 'modelo_diabetes.pkl')

# # Define the parameter grid
# param_grid = {
#     'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
#     'penalty': ['l1', 'l2'],
# }
#
# # Initialize the GridSearchCV
# grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='accuracy')
#
# # Fit the model
# grid_search.fit(X_train_scaled, y_train)
#
# # Get the best parameters
# best_params = grid_search.best_params_
#
# # Train the model with the best parameters
# model = LogisticRegression(**best_params)
# model.fit(X_train_scaled, y_train)
#
# # Evaluate the model
# predictions = model.predict(X_test_scaled)
# accuracy = accuracy_score(y_test, predictions)
# print(f'Acurácia: {accuracy}')


# # Inicializar e treinar o modelo
# model = LogisticRegression()
# model.fit(X_train_scaled, y_train)
#
# # Avaliação do modelo
# predictions = model.predict(X_test_scaled)
# accuracy = accuracy_score(y_test, predictions)
# print(f'Acurácia: {accuracy}')
#
#
# # Inicializar e treinar o modelo
# model = LogisticRegression()
# model.fit(X_train_scaled, y_train)
#
# # Avaliação do modelo
# predictions = model.predict(X_test_scaled)
# accuracy = accuracy_score(y_test, predictions)
# print(f'Acurácia: {accuracy}')
#
#
# # Salvar o modelo
# joblib.dump(model, 'modelo_diabetes.pkl')
#
#
# # Carregar o modelo (assumindo que já está na pasta correta)
# model = joblib.load('modelo_diabetes.pkl')
#
# # Criar inputs para o usuário inserir dados
# user_input1 = st.number_input('Insira o valor do primeiro recurso')
# # Repita para outros inputs conforme necessário
#
# # Quando estiver pronto para fazer uma predição
# if st.button('Prever'):
#     # Aqui você teria que ajustar os dados de entrada para corresponder ao modelo
#     prediction = model.predict([[user_input1, ...]])
#     st.write(f'Resultado da predição: {prediction}')

