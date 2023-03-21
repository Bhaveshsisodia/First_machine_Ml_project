from collections import namedtuple

# we will create a yaml file for reading all this as object

DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])
# Information of dataset coming and storing

DataValidationConfig = namedtuple("DataValidationConfig",["Schema_file_path"])
# Information about dataset like datatype and all

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                  "transformed_train_dir",
                                                                  "transformed_test_dir",
                                                                  "preprocessed_object_file_path"])
#pcike file path for tansformation
modelTrainingConfig = namedtuple("ModelTrainingConfig",["trained_model_file_path","base_accuracy"])
#pickle file save path second one is accepting and rejecting the model

modelEvaluationConfig = namedtuple("modelEvaluationConfig",["model_evaluation_file_path","time_stamp"]) # first one is path of all model where we can compare them

modelPusherConfig = namedtuple("modelPusherConfig",["export_dir_path"])

TrainingPipeLineConfig = namedtuple("TrainingPipeLineConfig", ["artifact_dir"])