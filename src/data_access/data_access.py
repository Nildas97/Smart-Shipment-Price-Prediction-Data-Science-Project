# FETCHING THE DATA FROM MONGODB DATABASE TO LOCAL MACHINE

# import libraries
import pandas as pd
import json
import os
import sys
from dotenv import load_dotenv
from src.logger import logging
import pymongo


def mongodb_client():
    # getting current root directory
    ROOT_DIR = os.getcwd()

    # getting the .env folder path
    ENV_FILE_PATH = os.path.join(ROOT_DIR, '.env')

    # loading the .env file
    load_dotenv(dotenv_path=ENV_FILE_PATH)

    # mongodb credentials
    username = os.getenv('USER_NAME')
    password = os.getenv('PASS_WORD')
    cluster_level = os.getenv('CLUSTER_LEVEL')

    # mongodb url link
    mongodb_url = f"mongodb+srv://{username}:{password}@{cluster_level}.mongodb.net/?retryWrites=true&w=majority"
    print(mongodb_url)

    # connecting to the mongodb database
    client = pymongo.MongoClient(mongodb_url)

    logging.info("Mongodb credentials are linked")

    return client
