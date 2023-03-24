from collections import namedtuple

<<<<<<< HEAD
# we will create a yaml file for reading all this as object

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["dataset_download_url", "tgz_download_dir"
                                  ,"raw_data_dir", "ingested_train_dir",
                                   "ingested_test_dir"])
# Information of dataset coming and storing

DataValidationConfig = namedtuple("DataValidationConfig", ["Schema_file_path"])
# Information about dataset like datatype and all

DataTransformationConfig = namedtuple("DataTransformationConfig",
                                        ["add_bedroom_per_room",
                                        "transformed_train_dir",
                                        "transformed_test_dir",
                                        "preprocessed_object_file_path"])
# pcike file path for tansformation
modelTrainingConfig = namedtuple(
    "ModelTrainingConfig", ["trained_model_file_path", "base_accuracy"])
# pickle file save path second one is accepting and rejecting the model

# first one is path of all model where we can compare them
modelEvaluationConfig = namedtuple("modelEvaluationConfig", [
                                   "model_evaluation_file_path", "time_stamp"])

modelPusherConfig = namedtuple("modelPusherConfig", ["export_dir_path"])

TrainingPipeLineConfig = namedtuple("TrainingPipeLineConfig", ["artifact_dir"])
=======
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_dir",
                                 "target_down_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

#### check the configuration of data coming 



DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

###### check(validate) the datatypes of the data we have


DataTranformationConfig = namedtuple("DataTranformationConfig",["add_bedroom_per_room",
                                 "transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])  
                                 
#### add_bedroom_per_room is calculated column, transformed_train_dir is directory of test and train data stored, file path of 
#### preprocessed data

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

##### pickel file od model saved at trained_model_file_path and base accuracy to surpass by the model

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file","time_stamp"])

###### model_evaluation_file contains all the information about the models that are in the production stage 
###### time_stamp is the time at which you do the comparison

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_model_path"])

##### if the new model perform better than all the models in production then we need to save and export  that model
##### as a pickle file

TraningPipelineConfig = namedtuple("TraningPipelineConfig",["artifact_dir"])
>>>>>>> ee80b54e30ac36b325799faea349fc0bb2371339
