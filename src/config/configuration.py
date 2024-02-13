from src.utils.logger import logging
from src.utils.utils import read_yaml, create_directory
from dataclasses import dataclass
from src.entity.config_entity import DataIngestionConfig, DataPreparationConfig, ModelTrainingConfig, ModelEvaluationConfig
import typing
from src.common import *
from pathlib import Path

    



class ConfigurationManager:
    """
    this class constructor is reponsible for getting the configuration data from the respective yaml file
    """
    def __init__(self):
        try:
            logging.warn('Inside the Configuration Manager')

            self.config_file = read_yaml(CONFIG_FILE_PATH)
            self.params_file = read_yaml(PARAMS_FILE_PATH)
            
            create_directory(Path(self.config_file['artifacts_folder']))

        except Exception as e:
            logging.error('Error in Configuration Manager class constructor')
            raise e

    def get_dataingestion_config(self) -> DataIngestionConfig:
        """
        this function gets the configuration details required for data ingestion process
        of type DataIngestionConfig class.
        """
        try:
            dataingestion_config = DataIngestionConfig(
                Path(self.config_file['data_ingestion']['data_folder']), 
                Path(self.config_file['data_ingestion']['local_folder']),
                Path(self.config_file['data_ingestion']['filename']))
            
            logging.critical("%s %s %s",self.config_file['data_ingestion']['data_folder'], self.config_file['data_ingestion']['local_folder'], self.config_file['data_ingestion']['filename'])
            
            return dataingestion_config
            
        except Exception as e:
            logging.error('Error in data_ingestion_config method')
            raise e



    def get_datapreparation_config(self):
        """
        this function gets the DataPreparationConfig details required for the performing
        datapreparation 
        """
        try:
            datapreparation_config = DataPreparationConfig(
                self.config_file['data_preparation']['unnecessary_columns'],
                Path(self.config_file['data_preparation']['filepath']),
                self.params_file['data_preparation']['test_size'],
                self.config_file['data_preparation']['label'],
                Path(self.config_file['data_preparation']['local_folder'])
            )
            return datapreparation_config

        except Exception as e:
            logging.error('Error in get_datapreparation_config method')
            raise e


    def get_modeltraining_config(self):
        try:
            modeltraining_config = ModelTrainingConfig(
                self.params_file['model_training']['alpha'],
                self.params_file['model_training']['l1_ratio'],
                Path(self.config_file['model_training']['filepath']),
                Path(self.config_file['model_training']['models_path']),
            )
            return modeltraining_config
        except Exception as e:
            raise e


    def get_modelevaluation_config(self):

        try:
            modelevaluation_config = ModelEvaluationConfig(
                self.params_file['model_training']['alpha'],
                self.params_file['model_training']['l1_ratio']
            )
            return modelevaluation_config
        except Exception as e:
            logging.error('Error while performing modelevaluation')
            raise e