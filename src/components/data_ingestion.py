from src.utils.logger import logging
import typing
from src.entity.config_entity import DataIngestionConfig
import shutil
from pathlib import Path
import os

class DataIngestion:
    """
    this class is responsible for perform the data ingestion process
    Here, it copies the data from self.config.data_folder to self.config.local_folder
    """

    def __init__(self, config: DataIngestionConfig):
        """
        this constructor receives DataIngestionConfig type variable as argument
        """
        self.config = config

    
    def process(self):
        """
        this method is responsible for copying the data from source 
        to destination folder as mentioned below

        """
        try:
            shutil.copy(self.config.data_folder, os.path.join(self.config.local_folder,self.config.filename))
            logging.info('Data Ingestion Process Completed Successfully....')
        except Exception as e:
            logging.critical('Error during Data Ingestion Process')
            raise e