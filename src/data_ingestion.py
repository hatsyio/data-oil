import requests
import yaml
from yaml.loader import FullLoader
from src.database import store_historical_data, store_lookup_data, try_transformation
from datetime import date, datetime, timedelta
import logging


def get_data(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or len(data) <= 0:
        error_message = (
            "Error fetching data on {} ".format(url)
            + "Status code: {}.".format(response.status_code)
            + "Num of fetched elements: {}.".format(len(data))
        )
        logging.error(error_message)
    return data


def load_conf():
    with open("conf/landing-ingestion.yml") as f:
        conf = yaml.load(f, Loader=FullLoader)
        return conf


def load_lookups():
    conf = load_conf()["lookups"]
    for collection_name in conf:
        url = conf[collection_name]
        data = get_data(url)
        store_lookup_data(data, collection_name)


def calculate_max_date() -> datetime.date:
    yesterday = date.today() - timedelta(days=1)
    return yesterday


def load_historical_data(
    start_date: datetime.date, end_date: datetime = calculate_max_date()
):
    conf = load_conf()["historical-data"]
    for collection_name in conf:
        url = conf[collection_name]
        while start_date <= end_date:
            date_str = start_date.strftime("%d-%m-%Y")
            data = get_data(url.format(date=date_str))
            store_historical_data(data, collection_name, start_date)
            start_date = start_date + timedelta(days=1)


def main():
    logging.info("Starting ingestion...")
    # load_lookups()
    
    #start_date = datetime.strptime("2007-01-01", '%Y-%m-%d').date()
    #print(start_date)
    #load_historical_data(start_date)

    try_transformation()
