import argparse
import os
import random
import logging
from src.utils.data_management import process_posts
from src.utils.utils import read_yaml, create_directories
import urllib.request as request
from configs.logging import logging

STAGE = "STAGE-02 prepare the data " 

def main(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    local_data_dir = config["source_download_dir"]["data_dir"]
    data_filename = config["source_download_dir"]["data_file"]
    input_data = os.path.join(local_data_dir, data_filename) 

    artifacts = config["artifacts"]
    prepared_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["PREPARED_DATA"])
    create_directories([prepared_data_dir_path])
    
    train_data_path = os.path.join(prepared_data_dir_path, artifacts["TRAIN_DATA"])
    test_data_path = os.path.join(prepared_data_dir_path, artifacts["TEST_DATA"])

    split = params["prepare_data"]["split"]
    seed = params["prepare_data"]["seed"]
    random.seed(seed)
    encoding = config['encoding']

    with open(input_data, encoding=encoding) as f_in:
        with open(train_data_path, "w", encoding=encoding) as f_out_train:
            with open(test_data_path, "w", encoding=encoding) as f_out_test:
                process_posts(f_in, f_out_train, f_out_test, "<python>", split)


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
