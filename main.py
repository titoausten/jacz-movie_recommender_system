import sys
from src import logger
from src.pipeline.stage_01_data_preprocessing import DataPreprocessingPipeline
from src.pipeline.stage_02_data_transformation import DataTransformationPipeline
from src.pipeline.stage_03_recommendation import RecommendationPipeline
from src.exceptions import CustomException


STAGE_NAME = "Data Preprocessing stage"
try: 
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   data_ingestion = DataPreprocessingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n[x==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n\n[x==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)


STAGE_NAME = "Recommendation Stage"
try: 
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   recommendation = RecommendationPipeline()
   recommendation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<]\n\n[x==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)
