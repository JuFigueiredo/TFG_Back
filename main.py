from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

import get_elements as ge
import svm as s

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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



# @app.get("/get-rna/{id}")
# def requisicao(id: str):
#     X_test = ge.getValues(id)
#     y_pred = s.svm(X_test["data"])
#     objeto = {
#         "personID": id,
#         "data": []
#     }
#     for i in y_pred:  # Número de Colunas
#         objeto["data"].append(int(i))
#     return objeto