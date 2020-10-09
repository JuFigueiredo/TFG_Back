from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient

import get_elements as ge
import svm as s

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Dale"}


@app.get("/getItems/{id}")
def requisicao(id: str):
    X_test = ge.getValues(id)
    y_pred = s.svm(X_test["data"])
    objeto = {
        "personID": id,
        "data": y_pred
    }
    # objeto = {
    #     "personID": id,
    #     "data": []
    # }
    # for i in y_pred:  # Número de Colunas
    #     objeto["data"].append(i)
    # return objeto



#  for item in y_pred:
#     print(item)