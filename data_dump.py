# DUMPING THE DATA FROM LOCAL MACHINE TO MONGODB DATABASE

# import libraries
import pandas as pd
import pymongo
import json
import os
from src.logger import logging


# mongodb client
# url = "mongodb+srv://nilutpalDAS992:s729TiAxVqw01pG@cluster0.xxk1zfm.mongodb.net/?retryWrites=true&w=majority"
# url = "mongodb+srv://DN56palsuit:9QX0yLYA8STzMRa3@cluster0.17pa9ai.mongodb.net/?retryWrites=true&w=majority"
url = "mongodb+srv://nilutpal809:0htrF5c27EpC3hG8pb@cluster0.vwlj2uf.mongodb.net/?retryWrites=true&w=majority"

# dataset name
DATABASE_NAME = "SMART_SHIPMENT"

# dataset folder name
COLLECTION_NAME = "SHIPMENT_DATA"

if __name__ == "__main__":

    # getting the current working directory
    ROOT_DIR = os.getcwd()

    # using the current working directory
    # getting the data file path by locating the data folder for dataset
    DATA_FILE_PATH = os.path.join(ROOT_DIR, "data", "train.csv")

    # using file path to get the data file path
    FILE_PATH = os.path.join(ROOT_DIR, DATA_FILE_PATH)

    # getting the schema data
    # write_schema_yaml(csv_file=DATA_FILE_PATH)

    # read the dataset
    df = pd.read_csv(DATA_FILE_PATH)  # referring to the old way
    print(f"Rows and columns: {df.shape}")

    # convert the dataframe into dictionaries
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    # establishing a connection to mongodb
    client = pymongo.MongoClient(url)

    # access the desired database and collection
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # inserting the json records into collection
    collection.insert_many(json_records)

    logging.info("Data pushed over mongodb database")

    # close the mongodb connection
    client.close()
