# CONSTANT FILE

# importing libraries
import os
import sys

# file name
FILE_NAME = "data.csv"

# getting current working directory
ROOT_DIR = os.getcwd()

# config directory
CONFIG_DIR = "configs"

# config_file name
SCHEMA_FILE = "config.yaml"

# complete config.yaml file path
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, SCHEMA_FILE)

# create variables related to data ingestion pipeline

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DATABASE_NAME = "database_name"
DATA_INGESTION_COLLECTION_NAME = "collection_name"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DATA_DIR_KEY = "ingested_train_data"
DATA_INGESTION_TEST_DATA_DIR_KEY = "ingested_test_data"
CONFIG_FILE_KEY = "configs"
