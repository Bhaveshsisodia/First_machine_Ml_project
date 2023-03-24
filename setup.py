### setup.py is important file for installing packages for housing folder
from setuptools import setup,find_packages
from typing import List






# Declaring Variables for setup functions
PROJECT_NAME="Housing_predictor"
VERSION = "0.0.1"
AUTHOR = 'Bhavesh'
DESCRIPTION = "This is my first machine learning end to end project"
PACKAGES= find_packages()
REQUIREMENT_FILE_NAME= "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention in requirements.txt file

    return this function is going to return a list which
    contain name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .\n')



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author =AUTHOR,
    description= DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)
