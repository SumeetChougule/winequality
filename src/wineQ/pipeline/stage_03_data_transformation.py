from src.wineQ.config.configuration import ConfigurationManager
from src.wineQ.components.data_transformation import DataTransformation
from src.wineQ import logging
from pathlib import Path

STAGE_NAME = "Data Transfromation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(
                    config=data_transformation_config
                )
                data_transformation.train_test_split()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)
