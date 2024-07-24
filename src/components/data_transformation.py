from src import logger
from src.utils.common import load_data
from src.entity.config_entity import DataTransformationConfig
from sklearn.feature_extraction.text import TfidfVectorizer


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.vectorizer = TfidfVectorizer()

    
    def calculate_tfidf_vectors(self, documents):
        # Calculate TF-IDF vectors for the documents
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        return tfidf_matrix
    