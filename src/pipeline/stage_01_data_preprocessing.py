from src.config.configuration import ConfigurationManager
from src.components.data_preprocessing import DataPreprocessing
from src.utils.common import get_size, save_data_to_csv, save_bin
from src import logger
from pathlib import Path
import os
import sys
from src.exceptions import CustomException


STAGE_NAME = "Data Preprocessing stage"


class DataPreprocessingPipeline:
    def __init__(self):
        pass

    def main(self):  
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()

        if not os.path.exists(data_preprocessing_config.local_data_path):
            data_preprocessing = DataPreprocessing(config=data_preprocessing_config)

            print(f"Creating new dataframe from important features...")
            new_data = data_preprocessing.create_new_dataframe()

            print(f"Creating new feature...")
            new_data = data_preprocessing.create_feature()

            print(f"Cleaning and preprocessing data..")
            new_data[data_preprocessing_config.new_feature] = new_data[data_preprocessing_config.new_feature].apply(data_preprocessing.preprocess_data)
            logger.info(f"Data cleaned and preprocessed")

            save_bin(new_data, data_preprocessing_config.movies_list_bin)
            save_data_to_csv(new_data, data_preprocessing_config.local_data_path)
        else:
            logger.info(f"File already exists of size: {get_size(Path(data_preprocessing_config.local_data_path))}")


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_transformation = DataPreprocessingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n[x==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)
