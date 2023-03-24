from housing.entity.config_entity import DataIngestionConfig,\
DataValidationConfig, DataTransformationConfig, modelTrainingConfig,\
modelEvaluationConfig, modelPusherConfig, TrainingPipeLineConfig

from housing.util.util import read_yaml_file
import sys
import os
from housing.constant import *
from housing.exception import HousingException
# for current working dir


class Configuration:

    def __init__(self,
                 config_file_path: str = CONFIG_FILE_PATH,
                 current_time_stamp: str = CURRENT_TIME_STAMP
                 ) -> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.get_training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> modelTrainingConfig:
        pass

    def get_model_evaluation_config(self) -> modelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> modelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipeLineConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
