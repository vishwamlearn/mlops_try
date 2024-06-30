import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys
#from sklearn.model_selection import train_test_split

from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self) -> None:
        pass
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
    