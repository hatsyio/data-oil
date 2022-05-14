from datetime import datetime
from pymongo import MongoClient
import logging


def get_database():
    db_uri = "mongodb://mongo:password@localhost:27017"
    client = MongoClient(db_uri)
    return client["data-oil-landing"]


def store_lookup_data(data: dict, collection_name: str):
    db = get_database()
    collection = db[collection_name]
    collection.drop()
    result = collection.insert_many(data)
    inserted_documents = len(result.inserted_ids)
    logging.info(
        "Collection {} loaded with {} entries.".format(
            collection_name, inserted_documents
        )
    )


def store_historical_data(data: dict, collection_name: str, date: datetime):
    db = get_database()
    collection_name_hist = collection_name + "/" + date.strftime("%Y-%m-%d")
    collection = db[collection_name_hist]
    print(collection_name_hist)
    collection.drop()
    collection.insert_one(data)
    logging.info(
        "Ingested data on collection {} for day {}.".format(collection_name, date)
    )


def try_transformation():
    db = get_database()
    collection = db["estaciones-terrestres"]
    res = collection.aggregate(
        [
            {"$unwind": "$ListaEESSPrecio"},
            {
                "$replaceRoot": {
                    "newRoot": {"$mergeObjects": ["$$ROOT", "$ListaEESSPrecio"]}
                }
            },
            {"$project": {"ListaEESSPrecio": 0, "_id": 0}},
        ]
    )
    for doc in res:
        print(doc)
        return
