from housing.entity.config_entity import DataIngestionConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging


class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            logging.info
