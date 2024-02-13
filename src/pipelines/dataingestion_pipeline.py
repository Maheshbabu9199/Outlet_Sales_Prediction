from src.utils.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager
from src.common import *
from src.components.data_ingestion import DataIngestion

Stage_name = 'Data_Ingestion_Stage'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def process(self):
        """
        this function is used to process the data ingestion pipeline
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_dataingestion_config()
            ingestion_stage = DataIngestion(config=data_ingestion_config)
            ingestion_stage.process()
            logging.info('Data Ingestion Pipeline Completed Successfully')
        except Exception as e:
            logging.error('Error during Data Ingestion Pipeline')
            raise e


if __name__ == '__main__':
    
    data_ingestion_pipe = DataIngestionPipeline()
    data_ingestion_pipe.process()