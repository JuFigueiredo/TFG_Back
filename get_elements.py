from pymongo import MongoClient


def getValues(id: str):
    # Open database connection
    client = MongoClient('localhost', 27017)
    dababase = client.veios_fall
    collection = dababase.test_data

    dale = collection.find({"userId": {"$eq": id}})

    matrix = []

    for item in dale:
        matrix.append(item["values"])

    objeto = {
        "personID": id,
        "data": matrix
    }

    return objeto
