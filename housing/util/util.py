import yaml

from housing.exception import HousingException
import os, sys

def read_yaml_file(file_path:str) -> dict:
    """
    Reads a yaml file and returns the contents as a dictionary file_path :str
    """
    try:
        with open(file_path,"rb") as yml_file:
            return yaml.safe_load(yml_file)
    except Exception as e :
        raise HousingException(e,sys) from e
