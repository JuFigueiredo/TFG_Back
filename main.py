from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient

import get_elements as ge

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Dale"}


@app.get("/getItems/{id}")
def requisicao(id: str):
    return ge.getValues(id)
