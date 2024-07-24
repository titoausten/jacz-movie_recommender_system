from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import (DataPreprocessingConfig,
                                      DataTransformationConfig,
                                      RecommendationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])


    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing
        create_directories([config.root_dir])

        data_preprocessing_config = DataPreprocessingConfig(
            root_dir=config.root_dir,
            source_data_path=config.source_data_path,
            local_data_path=config.local_data_path,
            movies_list_bin=config.movies_list_bin,
            important_feature=config.important_feature,
            important_feature1=config.important_feature1,
            important_feature2=config.important_feature2,
            important_feature3=config.important_feature3,
            new_feature=config.new_feature
        )

        return data_preprocessing_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            source_data_path=config.source_data_path,
            vector_similarity_path=config.vector_similarity_path
        )

        return data_transformation_config


    def get_recommendation_config(self) -> RecommendationConfig:
        config = self.config.recommendation

        data_recommendation_config = RecommendationConfig(
            movies_list_path=config.movies_list_path,
            vector_similarity_path=config.vector_similarity_path,
            movie_id_url=config.movie_id_url,
            poster_url=config.poster_url 
        )

        return data_recommendation_config
