# HELPER FUNCTIONS

# import libraries
import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from datetime import datetime
from src.constant import *
import yaml
from src.data_access.data_access import mongodb_client


def read_yaml_file(file_path: str) -> dict:
    try:

        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys)


def get_collection_as_dataframe(database_name: str, collection_name: str) -> pd.DataFrame:
    try:
        client = mongodb_client()

        df = pd.DataFrame(list(client[database_name][collection_name].find()))

        if "_id" in df.columns:
            df = df.drop("_id", axis=1)
            return df

    except Exception as e:
        raise CustomException(e, sys)
