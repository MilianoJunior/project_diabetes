from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import dotenv

dotenv.load_dotenv()

class Item(BaseModel):
    Pregnancies: str
    Glucose: str
    BloodPressure: str
    SkinThickness: str
    Insulin: str
    BMI: str
    DiabetesPedigreeFunction: str
    Age: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/salvarinteracao")
def salvar_interacao(data):
    # salvar a interação
    # retornar a interação
    return data

@app.post("/predict/")
def predict(item: Item):
    # carregar o modelo
    model = joblib.load('../assets/modelo_diabetes.pkl')
    # fazer a predição
    item = item.dict()
    item = pd.DataFrame(item, index=[0])
    prediction = model.predict(item)
    # retornar a predição
    return {"prediction": int(prediction[0])}

    return {"Pregnancies": item.Pregnancies, "Glucose": item.Glucose, "BloodPressure": item.BloodPressure, "SkinThickness": item.SkinThickness, "Insulin": item.Insulin, "BMI": item.BMI, "DiabetesPedigreeFunction": item.DiabetesPedigreeFunction, "Age": item.Age}

if __name__ == '__main__':
    import os
    import uvicorn
    uvicorn.run(app, host=os.getenv('UVICORN_URL'), port=int(os.getenv('UVICORN_PORT')))