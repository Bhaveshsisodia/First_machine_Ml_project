from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os
import json
import sys
from housing.util.util import read_yaml_file

import pandas as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab


class DataValidation:

    def __init__(self, data_validation_config: DataValidationConfig, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys) from e

    def get_train_and_test_dataframe(self):
        try:
            train_df = pd.read_csv(
                self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_train_test_file_exists(self):
        try:
            logging.info("Checking if training and test file is available...")
            is_train_file_exists = False
            is_test_file_exists = False
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            print(train_file_path,test_file_path)

            is_train_file_exists = os.path.exists(train_file_path)
            is_test_file_exists = os.path.exists(test_file_path)

            is_available = is_train_file_exists and is_test_file_exists

            logging.info(f"Is train and test file exists? -> {is_available}")

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file:{training_file} or Testing File :{testing_file} \
                    is not available"
                raise Exception(message)
            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e

    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False

            train_df, test_df = self.get_train_and_test_dataframe()
            print(self.data_validation_config.schema_file_path)
            schema_file_read = read_yaml_file(
                file_path=self.data_validation_config.schema_file_path)
            col=schema_file_read['columns']
            dict_data = json.loads(json.dumps(col))
            dom_val=schema_file_read['domain_value']
            dom_val=list(dom_val.values())[0]



# Count the number of keys in the dictionary
            num_keys = len(dict_data.keys())

            condition1 =(all(x in list(dict_data.keys()) for x in list(train_df.columns))) and  (all(x in list(dict_data.keys()) for x in list(test_df.columns)))
            # condition= (list(train_df.columns) in  list(dict_data.keys())) and (list(test_df.columns) in  list(dict_data.keys()))
            condition2 = (len(test_df.columns) == int(num_keys-1)) and (len(train_df.columns) == int(num_keys-1))
            condition3 = schema_file_read['target_column'] in train_df.columns


            condition4 =set(dom_val) ==  set(train_df['ocean_proximity'].unique().tolist())

            # assignment validate training and testing dataset using schema file
            # 1 Number of column
            # 2 check the value of ocean proximity
            # acceptable values
            # 3 check column names
            if condition1 and condition2 and condition3 and condition4:
                validation_status = True
            else:
                validation_status= False
            logging.info(f"validation_status ----->{validation_status}")
            return validation_status
            # return validation_status

        except Exception as e:
            raise HousingException(e, sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df, test_df = self.get_train_and_test_dataframe()

            profile.calculate(train_df, test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir, exist_ok=True)

            with open(report_file_path, "w") as report_file:
                json.dump(report, report_file, indent=6)

            return report

        except Exception as e:
            raise HousingException(e, sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df, test_df = self.get_train_and_test_dataframe()
            dashboard.calculate(train_df, test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path

            report_page_dir = os.path.dirname(report_page_file_path)

            os.makedirs(report_page_dir, exist_ok=True)
            dashboard.save(self.data_validation_config.report_page_file_path)
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_data_drift_found(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()

            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated="True",
                message="Data Validation Performed Successfully"
            )

            logging.info(
                f"Data Validation artifact:[{data_validation_artifact}]")

        except Exception as e:
            raise HousingException(e, sys) from e
