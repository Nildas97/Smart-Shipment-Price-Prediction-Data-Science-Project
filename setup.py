# SETTING UP SETUP FILE 

# importing libraries
from setuptools import setup, find_packages
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# defining function to get all requirement
def get_requirements()->List[str]:
    
    # opening the requirement.txt file
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        
        # reading line by line of requirement.txt file
        requirement_list = requirement_file.readlines()
    
    # replacing "\n" with "empty space" in requirement.txt
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    
    # if statement to remove HYPHEN_E_DOT from requirement.txt
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


# setup file description
setup(name="Smart Shipment Price Prediction",
      version="0.0.1",
      description="Data Science Project",
      author="Nilutpal Das",
      author_email="nilutpaldas992@gmail.com",
      packages=find_packages(),
      install_requirements=[]
)