# PIPELINE


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
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.components.data_ingestion import DataIngestion


class Pipeline():

    def __init__(self, training_pipeline_config=TrainingPipelineConfig()) -> None:
        try:
            self.training_pipeline_config = training_pipeline_config

        except Exception as e:
            raise CustomException(e, sys)

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=DataIngestionConfig(self.training_pipeline_config))
            logging.info("Starting data ingestion")
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys)
