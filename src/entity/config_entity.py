# CONFIG ENTITY

# import libraries
import os
import sys
from src.exception import CustomException
from src.logger import logging
from datetime import datetime
from src.constant import *
from src.utils import read_yaml_file

# to read config.yaml file
# using config_file_path from constant directory
config_data = read_yaml_file(CONFIG_FILE_PATH)


class TrainingPipelineConfig:
    # defining constructor
    def __init__(self):
        try:
            # defining artifact dir
            # first, getting current working dir
            # then create artifact dir using datetime format
            self.artifact_dir = os.path.join(
                os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise CustomException(e, sys)


class DataIngestionConfig:

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:

            # defining data ingestion key
            data_ingestion_key = config_data[DATA_INGESTION_CONFIG_KEY]

            # defining database name
            self.database_name = data_ingestion_key[DATA_INGESTION_DATABASE_NAME]

            # defining collection name
            self.collection_name = data_ingestion_key[DATA_INGESTION_COLLECTION_NAME]

            # defining data ingestion directory
            self.data_ingestion_dir = os.path.join(
                training_pipeline_config.artifact_dir, data_ingestion_key[DATA_INGESTION_ARTIFACT_DIR])

            # defining raw data directory
            self.raw_data_dir = os.path.join(
                self.data_ingestion_dir, data_ingestion_key[DATA_INGESTION_RAW_DATA_DIR_KEY])

            # defining ingested directory
            self.ingested_data_dir = os.path.join(
                self.raw_data_dir, data_ingestion_key[DATA_INGESTION_INGESTED_DATA_DIR_KEY])

            # defining train data file path
            self.train_file_path = os.path.join(
                self.ingested_data_dir, data_ingestion_key[DATA_INGESTION_TRAIN_DATA_DIR_KEY])

            # defining test data file path
            self.test_file_path = os.path.join(
                self.ingested_data_dir, data_ingestion_key[DATA_INGESTION_TEST_DATA_DIR_KEY])

            # defining test data size
            self.test_size = 0.2

        except Exception as e:
            raise CustomException(e, sys)
