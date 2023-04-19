from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", ["dataset_download_dir",
                                 "tgz_download_dir", "raw_data_dir", "ingested_train_dir", "ingested_test_dir"])

# check the configuration of data coming


DataValidationConfig = namedtuple("DataValidationConfig", [
                                  "schema_file_path", "report_file_path", "report_page_file_path"])

# check(validate) the datatypes of the data we have


DataTransformationConfig = namedtuple("DataTranformationConfig", ["add_bedroom_per_room",
                                                                  "transformed_train_dir", "transformed_test_dir",
                                                                    "preprocessed_object_file_path"])

# add_bedroom_per_room is calculated column, transformed_train_dir is directory of test and train data stored, file path of
# preprocessed data

ModelTrainingConfig = namedtuple(
    "ModelTrainerConfig", ["trained_model_file_path", "base_accuracy"])

# pickel file od model saved at trained_model_file_path and base accuracy to surpass by the model

modelEvaluationConfig = namedtuple("ModelEvaluationConfig", [
                                   "model_evaluation_file", "time_stamp"])

# model_evaluation_file contains all the information about the models that are in the production stage
# time_stamp is the time at which you do the comparison

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_model_path"])

# if the new model perform better than all the models in production then we need to save and export  that model
# as a pickle file

TraningPipelineConfig = namedtuple("TraningPipelineConfig", ["artifact_dir"])
