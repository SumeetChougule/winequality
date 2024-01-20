from src.wineQ.config.configuration import ConfigurationManager
from src.wineQ.components.model_evaluation import ModelEvaluation
from src.wineQ import logging

STAGE_NAME = "Model evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_data_model_evaluation_config()
        model_eval_config = ModelEvaluation(config=model_eval_config)
        model_eval_config.log_into_mlflow()


if __name__ == "__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
