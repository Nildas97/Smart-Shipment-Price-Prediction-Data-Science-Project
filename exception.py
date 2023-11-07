# DEMO FLASK APP FOR EXCEPTION FILE TESTING

# importing libraries
from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os
import sys


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our exception file")
    except Exception as e:

        ML = CustomException(e, sys)

        logging.info(ML.error_message)

        logging.info("we are testing our exception file")

        return "Success Analytics Project Bootcamp batch"


if __name__ == "__main__":
    app.run(debug=True)
