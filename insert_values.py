from pymongo import MongoClient
import pandas as pd


# Abrir arquivos
Ids = open("subject_id_test.txt", "r").read().split("\n")
xTrain = pd.read_csv("X_test.txt", sep=" ", header=None)
yTest = open("y_test.txt", "r").read().split("\n")

# Conectar no DB (ip , porta)
client = MongoClient('localhost', 27017)

# Nome do seu DB
dababase = client.veios_fall


# Nome da sua collection
collection = dababase.test_data

index = 0


for i in range(3160):  # Número de Linhas
    dataSet = {
        "userId": Ids[i],
        "values": [],
        "res": yTest[i]
    }
    for j in range(561):  # Número de Colunas
        dataSet["values"].append(xTrain[j][i])

    collection.insert_one(dataSet)

# print(dataSet["values"])

print("Done")
