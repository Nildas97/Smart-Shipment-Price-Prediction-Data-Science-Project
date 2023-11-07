# LOGGER FILE SETUP

# import libraries
import logging
import os
import sys
from datetime import datetime

# log file directory name
LOG_DIR = "logs"

# creating log file directory
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)

# log file name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"

# log file name format
file_name = f"log{CURRENT_TIME_STAMP}.log"

# log file path
log_file_path = os.path.join(LOG_DIR, file_name)

# log file configuration
logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
