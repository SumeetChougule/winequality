from src.wineQ import logging

from src.wineQ import logging
from src.wineQ.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wineQ.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.wineQ.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)

from src.wineQ.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

# from src.wineQ.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logging.exception(e)
    raise e
