from src.utils.logger import logging
from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation 



class ModelEvaluation_Pipeline:
    def __init__(self):
        pass

    def process(self):
        config = ConfigurationManager()
        modelevaluation_config = config.get_modelevaluation_config()
        model_evaluation = ModelEvaluation(config=modelevaluation_config)



if __name__ == '__main__':
    model_evaluation = ModelEvaluation_Pipeline()
    model_evaluation.process()