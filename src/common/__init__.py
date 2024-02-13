from pathlib import Path
import os
from src.utils.logger import logging

logging.warn("%s", os.getcwd())

CONFIG_FILE_PATH = Path("src\config\config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

logging.info("%s", CONFIG_FILE_PATH)
logging.info('%s', PARAMS_FILE_PATH)