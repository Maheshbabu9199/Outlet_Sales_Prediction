from src.utils.logger import logging
from src.config.configuration import ConfigurationManager
from src.entity.config_entity import  DataPreparationConfig
from src.components.data_preparation import DataPreparation 

Stage_name = 'Data_Preparation_stage'

class DataPreparation_Pipeline:
    def __init__(self):
        pass

    def process(self):
        config = ConfigurationManager()
        datapreparation_config = config.get_datapreparation_config()
        preparation_stage = DataPreparation(config=datapreparation_config)
        preparation_stage.process()

        


if __name__ == '__main__':
    preparation_pipeline = DataPreparation_Pipeline()
    preparation_pipeline.process()
