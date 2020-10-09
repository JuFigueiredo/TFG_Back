from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient

import get_elements as ge
import svm as s

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Dale"}


@app.get("/get-svm/{id}")
def requisicao(id: str):
    X_test = ge.getValues(id)
    y_pred = s.svm(X_test["data"])
    objeto = {
        "personID": id,
        "data": []
    }
    for i in y_pred:  # Número de Colunas
        objeto["data"].append(int(i))
    return objeto