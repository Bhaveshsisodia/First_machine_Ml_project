from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.exception import HousingException
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # schema_file_path = r"C:\Users\dell\First_machine_Ml_project\config\schema.yaml"
        # file_path = r"C:\Users\dell\First_machine_Ml_project\housing\artifact\data_ingestion\2023-04-11-01-34-35\ingested_data\train\housing.csv"

        # df=DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == '__main__':
    main()
