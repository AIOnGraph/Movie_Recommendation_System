import pandas as pd
import streamlit as st
import joblib
from streamlit_tags import st_tags

st.set_page_config(layout="wide")

movies = joblib.load('movie_list1.joblib')
similarity = joblib.load('similarity1.joblib')

movies['Movie_Title'] = movies['Movie_Title'].apply(lambda x: x.lower())
movies['Director'] = movies['Director'].apply(lambda x: x.lower())
movies['main_genre'] = movies['main_genre'].apply(lambda x: x.lower())
movies['Actors'] = movies['Actors'].apply(lambda x: x.lower())


all_actors = set()
for actors in movies['Actors']:
    all_actors.update(actors.split(', '))
all_actors = list(all_actors)


movie_suggestions = movies['Movie_Title'].unique().tolist()
director_suggestions = movies['Director'].unique().tolist()
genre_suggestions = movies['main_genre'].unique().tolist()
actors_suggestions = all_actors

st.title('**🎬 Movie Recommendation System**')
st.write("### Welcome to our movie recommendation system! Type a movie, director, genre, or actor, and we'll recommend similar movies for you.")

selected_item = st.selectbox('Search for a Movie, Director, Genre, or Actor:', [''] + movie_suggestions + director_suggestions + genre_suggestions + actors_suggestions)

def recommendation(selected_item):
    try:
        selected_item_lower = selected_item.lower()
        if selected_item_lower in movies['Movie_Title'].values:
            index = movies[movies['Movie_Title'] == selected_item_lower].index[0]
        elif selected_item_lower in movies['Director'].values:
            index = movies[movies['Director'] == selected_item_lower].index[0]
        elif selected_item_lower in movies['main_genre'].values:
            index = movies[movies['main_genre'] == selected_item_lower].index[0]
        elif selected_item_lower in all_actors:
            index = movies[movies['Actors'].str.contains(selected_item_lower)].index[0]
        else:
            return []
        
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommended_movies = []
        for i in distance[1:6]:
            recommended_movies.append(movies.iloc[i[0]].Movie_Title)
        return recommended_movies
    except IndexError:
        return []

if selected_item:
    movie_names = recommendation(selected_item)
    if movie_names:
        st.write("**Recommended Movies:**")
        for i, movie in enumerate(movie_names, start=1):
            st.write(f"{i}. ##### {movie}")
    else:
        st.write("Please enter a correct movie, director, genre, or actor.")