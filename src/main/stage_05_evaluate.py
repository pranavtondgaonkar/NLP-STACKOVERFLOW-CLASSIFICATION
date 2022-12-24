import argparse
import os
import joblib
import logging
from src.utils.utils import read_yaml, save_json
import numpy as np
import sklearn.metrics as metrics
import math
from configs.logging import logging


STAGE = "STAGE-05 Evaluation" 

def main(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info(f"stage {STAGE} started")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f"stage {STAGE} completed!")
    except Exception as e:
        logging.exception(e)
        raise e
