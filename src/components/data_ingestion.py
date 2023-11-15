# DATA INGESTION

# import libraries
import os
import sys
import shutil
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.utils import read_yaml_file, get_collection_as_dataframe
from sklearn.model_selection import train_test_split
from src.constant import *


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info("Data Ingestion Started")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def get_data_from_mongodb(self):

        # 1. getting the data from mongodb
        # defining the database name and collection name
        logging.info("Exporting collection data as pandas dataframe")
        df: pd.DataFrame = get_collection_as_dataframe(
            database_name=self.data_ingestion_config.database_name,
            collection_name=self.data_ingestion_config.collection_name)

        # 2. saving the data into raw data directory
        # defining raw data directory
        logging.info("Calling the raw data dir")
        raw_data_dir = self.data_ingestion_config.raw_data_dir

        # creating raw data directory
        logging.info(f" Raw Data directory : {raw_data_dir}")
        os.makedirs(raw_data_dir, exist_ok=True)

        # defining csv file name
        csv_file_name = 'train.csv'

        # defining the raw data file path
        # using raw data directory along with csv file name
        raw_file_path = os.path.join(raw_data_dir, csv_file_name)

        # saving the csv file
        df.to_csv(raw_file_path)

        # 3. defining ingested data directory
        # saving a copy of entire raw data into it
        ingested_data_dir = os.path.join(
            self.data_ingestion_config.ingested_data_dir)

        # creating ingested data directory
        logging.info(f" Ingested Data directory : {ingested_data_dir}")
        os.makedirs(ingested_data_dir, exist_ok=True)

        # defining the ingested data file path
        # using ingested data directory along with csv file name
        ingested_file_path = os.path.join(
            self.data_ingestion_config.ingested_data_dir, csv_file_name)

        # 4. creating a copy of raw data in ingested data dir
        # copying from raw data dir to ingested data dir
        shutil.copy2(raw_file_path, ingested_file_path)

        logging.info("Data stored in Raw Data and Ingested Data Directory")

        return ingested_file_path

    def split_train_and_test(self, csv_file_name):

        # defining the train and test file path
        logging.info("Defining the train data and test data path")
        train_file_path = self.data_ingestion_config.train_file_path
        test_file_path = self.data_ingestion_config.test_file_path

        # creating train and test file path
        os.makedirs(train_file_path)
        os.makedirs(test_file_path)

        # to split the data, first read the data
        # reading the data
        data = pd.read_csv(csv_file_name, index_col=0)

        # defining the test size
        size = self.data_ingestion_config.test_size

        # calling train_test_split function
        logging.info("Splitting the data into train and test data")
        train_data, test_data = train_test_split(
            data, test_size=size, random_state=42)

        # defining the train and test data file name
        train_file_path = os.path.join(train_file_path, FILE_NAME)
        test_file_path = os.path.join(test_file_path, FILE_NAME)

        # saving the train and test data
        train_data.to_csv(train_file_path, index=False)
        test_data.to_csv(test_file_path, index=False)

        # calling the data_ingestion_artifact function
        # to get the desired output in str format
        data_ingestion_artifact = DataIngestionArtifact(
            train_file_path=train_file_path,
            test_file_path=test_file_path)

        logging.info(f" Train File path : {train_file_path}")
        logging.info(f" Test File path : {test_file_path}")

        return data_ingestion_artifact

    def initiate_data_ingestion(self):

        try:
            logging.info("Donwloading data from mongo ")

            ingested_file_path = self.get_data_from_mongodb()

            logging.info("Splitting data .... ")

            return self.split_train_and_test(csv_file_name=ingested_file_path)

        except Exception as e:
            raise CustomException(e, sys)
