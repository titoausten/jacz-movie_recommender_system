from src.config.configuration import ConfigurationManager
from src.components.recommendation import Recommendation
from src import logger
import sys
from src.exceptions import CustomException


STAGE_NAME = "Recommendation stage"


class RecommendationPipeline:
    def __init__(self):
        pass
    

    def main(self):  
        config = ConfigurationManager()
        recommendation_config = config.get_recommendation_config()
        recommendation = Recommendation(config=recommendation_config)
        movie_title = input("Enter Movie Title: ")
        logger.info(f"Getting recommendations based on {movie_title}...")
        recommendations = recommendation.recommend_movies(movie_title)
        logger.info(f"Recommendations based on {movie_title} found.")
        print(f'Top 5 recommended Movies for {movie_title}:\n{recommendations}')


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        recommendation = RecommendationPipeline()
        recommendation.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n\n[x==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)
