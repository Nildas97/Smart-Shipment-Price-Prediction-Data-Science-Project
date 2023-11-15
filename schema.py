# GENERATING YAML FILE FOR THE DATASET

# import libraries
import yaml
import os
import sys
import pandas as pd


def write_schema_yaml(csv_file):

    df = pd.read_csv(csv_file)

    num_cols = len(df.columns)

    cols_name = df.columns.tolist()

    cols_dtypes = df.dtypes.astype(str).tolist()

    schema = {
        "File_name": os.path.basename(csv_file),
        "No_of_cols": num_cols,
        "Cols_names": dict(zip(cols_name, cols_dtypes))
    }

    # write schema to schema.yaml

    # getting the current working directory
    ROOT_DIR = os.getcwd()

    # using current working directory
    # locating inside the root directory, under configs folder is schema.yaml
    SCHEMA_PATH = os.path.join(ROOT_DIR, 'configs', 'schema.yaml')

    # open the schema.yaml file as write mode to dump the data
    with open(SCHEMA_PATH, "w") as file:
        yaml.dump(schema, file)
