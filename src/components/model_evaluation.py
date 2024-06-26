import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn

from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluationn:
    def __init__(self) -> None:
        pass
    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
    