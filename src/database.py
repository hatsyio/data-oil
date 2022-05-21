from datetime import datetime
from pymongo import MongoClient
from sqlalchemy import create_engine
import pandas as pd
import unidecode
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


def get_collection_data(collection_name: str) -> pd.DataFrame:
    db = get_database()
    collection = db[collection_name]
    return pd.DataFrame(list(collection.find([], {'_id': False})))


def sanitize_name(name: str) -> str:
    result = name.replace('-', '_')
    result = result.replace(' ', '_')
    result = result.replace('%', 'porcentaje')
    # remove accents
    result = unidecode.unidecode(result)
    return result


def load_staging(data: pd.DataFrame, collection_name, is_lookup):
    engine = create_engine('postgresql://postgres:password@localhost:5432/data-oil', echo=True)
    insert_type = "replace" if is_lookup else "append"
    result = data.to_sql(name=sanitize_name(collection_name), con=engine, schema='data_oil_stg', if_exists=insert_type, index=False)

    # db = get_database()
    # collection = db["estaciones-terrestres"]
    # res = collection.aggregate(
    #     [
    #         {"$unwind": "$ListaEESSPrecio"},
    #         {
    #             "$replaceRoot": {
    #                 "newRoot": {"$mergeObjects": ["$$ROOT", "$ListaEESSPrecio"]}
    #             }
    #         },
    #         {"$project": {"ListaEESSPrecio": 0, "_id": 0}},
    #     ]
    # )
    # for doc in res:
    #     print(doc)
    #     return
