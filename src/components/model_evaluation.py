from src.utils.logger import logging




class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def process(self):
        with mlflow.start_run():
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)
    