import numpy as np
import requests
from src import logger
from src.utils.common import load_bin
from src.entity.config_entity import RecommendationConfig


class Recommendation:
    def __init__(self, config: RecommendationConfig):
        self.config = config
        # Load movies data
        self.movies = load_bin(self.config.movies_list_path)
        self.movies_titles = self.movies['title'].values
        # Load Similarity Vector Data
        self.vector_similarity = load_bin(self.config.vector_similarity_path)


    def fetch_poster(self, movie_id: int):
        url = self.config.movie_id_url.format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = self.config.poster_url + poster_path
        return full_path


    def recommend_movies(self, movie_title: str, get_poster: bool = False):
        # find movie id
        movie_index = np.where(self.movies_titles == movie_title)[0][0]
        # get movie similarities
        movie_similarities = self.vector_similarity.iloc[movie_index].values
        # get top 5 similar movie IDs
        similar_movie_idxs = np.argsort(-movie_similarities)[1:6]
        # get top 5 movies
        similar_movies = self.movies_titles[similar_movie_idxs]

        # Fetch corresponding IDs from the dataframe
        similar_movies_ids = [self.movies[self.movies['title'] == title].iloc[0].id for title in similar_movies]

        if get_poster:
            similar_movie_posters = []
            # Fetch corresponding poster
            logger.info(f"Fetching movie posters...")
            for id in similar_movies_ids:
                similar_movie_posters.append(self.fetch_poster(id))
            logger.info(f"Movie posters fetched.")
            return similar_movies, similar_movie_posters
        
        else:
            # Combine movie titles and IDs
            similar_movies_with_ids = [f"{title} (ID: {movie_id})" for title, movie_id in zip(similar_movies, similar_movies_ids)]
            similar_movies_str = "\n".join(similar_movies_with_ids)

            # return the top 5 movies
            return similar_movies_str
