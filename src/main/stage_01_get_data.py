import argparse
import os
import logging
from src.utils.utils import read_yaml, create_directories
import urllib.request as request
from configs.logging import logging


STAGE = "STAGE-01 get data from S3 bucket" 


def main(config_path):
    config = read_yaml(config_path)
    source_data_url = SOURCE_DATA_URL
    local_data_dir = config["source_download_dir"]["data_dir"]
    data_filename = config["source_download_dir"]["data_file"]

    create_directories([local_data_dir])    
    local_data_filepath = os.path.join(local_data_dir, data_filename)
    logging.info("Download started")
    filename, headers = request.urlretrieve(source_data_url, local_data_filepath)
    logging.info(f"Download completed, file present at {local_data_filepath}")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info(f"stage {STAGE} started")
        main(config_path=parsed_args.config)
        logging.info(f"stage {STAGE} completed!")
    except Exception as e:
        logging.exception(e)
        raise e
