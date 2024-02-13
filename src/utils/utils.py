from src.utils.logger import logging
import typing 
from ensure import ensure_annotations
from pathlib import Path
import yaml
import os
import pandas as pd
import pickle
from sklearn.base import BaseEstimator

@ensure_annotations
def read_yaml(filename: Path):
    """
    this function accepts the yaml file and reads the data,
    returns the content of the yaml file
    """
    try:
        with open(filename, 'r') as f:
            config_content = yaml.safe_load(f)
        logging.info(f'Reading {filename} has been completed')
        return config_content
    except Exception as e:
        logging.error(f'Error while reading {filename}')
        raise e


@ensure_annotations
def create_directory(directory_name: Path):
    """
    this function is used to create a directories
    accepts the directory name as string 
    """
    try:
        os.makedirs(directory_name, exist_ok=True)
    except Exception as e:
        logging.error('Error while creating directory: %s', directory_name)
        raise e
    

@ensure_annotations
def save_tocsv(data : pd.DataFrame, location : Path, filename : str):
    file = os.path.join(location, filename)
    data.to_csv(file)
    logging.info("%s saved", filename)

@ensure_annotations
def save_models(model: BaseEstimator, filename: str, models_path: Path):
    filename = os.path.join(models_path, filename)
    pickle.dump(model, open(filename, 'wb'))
    logging.info("%s saved model %s" % (filename, model))