import pandas as pd
import streamlit as st
import joblib
from streamlit_tags import st_tags

st.set_page_config(layout="wide")

movies = joblib.load('movie_list1.joblib')
similarity = joblib.load('similarity1.joblib')
movies_list = [title.lower() for title in movies['Movie_Title'].values.tolist()]

st.title('**🎬 Movie Recommendation System**')
st.write("### Welcome to our movie recommendation system! Select a movie from the dropdown list, and we'll recommend similar movies for you.")

selected_movies = st_tags(
    label='## Select a Movie:',
    text='Press enter',
    value=[],
    suggestions=movies_list,
    maxtags=1
)

def recommendation(movie):
    movie = movie.lower()
    try:
        index = movies[movies['Movie_Title'].str.lower() == movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommended_movies = []
        for i in distance[1:6]:
            recommended_movies.append(movies.iloc[i[0]].Movie_Title)
        return recommended_movies
    except IndexError:
        return []

if selected_movies:
    movie_name = recommendation(selected_movies[0])
    if movie_name:
        st.write("**Recommended Movies:**")
        for i, movie in enumerate(movie_name, start=1):
            st.write(f"{i}. ##### {movie}")
    else:
        st.write("Please enter the correct movie name.")
