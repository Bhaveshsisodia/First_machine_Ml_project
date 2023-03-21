from housing.entity.config_entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig \
, modelTrainingConfig , modelEvaluationConfig , modelPusherConfig , TrainingPipeLineConfig

class Configuration:

    def __init__(self) -> None:
        pass

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
        pass