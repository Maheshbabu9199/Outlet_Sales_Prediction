from src.utils.logger import logging
from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTraining




class ModelTrainingPipeline:
    def __init__(self):
        pass

    def process(self):
        config = ConfigurationManager()
        modeltraining_config = config.get_modeltraining_config()
        model_training = ModelTraining(config=modeltraining_config)
        model_training.process()


if __name__ == '__main__':
    modeltraining = ModelTrainingPipeline()
    modeltraining.process()