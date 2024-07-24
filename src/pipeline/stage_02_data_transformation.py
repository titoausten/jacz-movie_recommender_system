import os
import sys
import pandas as pd
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.utils.common import get_size, save_data_to_csv, save_bin, load_data
from src import logger
from pathlib import Path
from src.exceptions import CustomException
from sklearn.metrics.pairwise import cosine_similarity


STAGE_NAME = "Data Transformation stage"


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):  
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()

        if not os.path.exists(data_transformation_config.vector_similarity_path):
        
            data_transformation = DataTransformation(config=data_transformation_config)
            data = load_data(data_transformation_config.source_data_path)
            data = data.reset_index(drop=True)
            # Remove rows with NaN values in the 'description' column
            data = data.dropna(subset=['description'])

            # Calculate TF-IDF vectors for the documents
            logger.info(f"Feature Extraction started...")
            tfidf_matrix = data_transformation.calculate_tfidf_vectors(data['description'])
            logger.info(f"Feature Extraction complete.")

            logger.info(f"Calculating Cosine Similarity...")
            similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            similarity_matrix = pd.DataFrame(similarity_matrix)
            logger.info(f"Cosine Similarity calculation complete.")

            save_bin(similarity_matrix, data_transformation_config.vector_similarity_path)
        else:
            logger.info(f"File already exists of size: {get_size(Path(data_transformation_config.vector_similarity_path))}")



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        data_transformation = DataTransformationPipeline()
        data_transformation.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n\n[x==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)
