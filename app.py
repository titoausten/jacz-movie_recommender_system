import streamlit as st
from src.config.configuration import ConfigurationManager
from src.components.recommendation import Recommendation
from src.utils.common import set_background


def main():
    st.set_page_config(page_title="JacZ Movie Recommender")
    set_background('artifacts/images/background.jpg')
    st.header('Movie Recommender System by JacZ')

    config = ConfigurationManager()
    recommendation_config = config.get_recommendation_config()
    recommender = Recommendation(config=recommendation_config)

    movies_titles = recommender.movies_titles

    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movies_titles
        )

    if st.button('Show Recommendation'):
        recommended_movie_titles, recommended_movie_posters = recommender.recommend_movies(selected_movie, get_poster=True)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(recommended_movie_titles[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_titles[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_titles[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_titles[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_titles[4])
            st.image(recommended_movie_posters[4])


if __name__ == '__main__':
    main()
