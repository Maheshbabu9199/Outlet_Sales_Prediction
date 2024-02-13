from dataclasses import dataclass
from src.utils.logger import logging
import typing
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    this class holds the details/variables required for the data ingestion process
    """
    data_folder: Path
    local_folder: str
    filename: str

    logging.warn('DataIngestionConfig class loaded')
    


@dataclass(frozen=True)
class DataPreparationConfig:
    unncessary_columns: list
    filepath : Path
    test_size: float
    label: str
    local_folder: Path



@dataclass(frozen=True)
class ModelTrainingConfig:
    alpha: float
    l1_ratio: float
    filepath : Path
    models_path: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    alpha: float
    l1_ratio: float
    