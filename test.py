import pandas as pd
import streamlit as st
import joblib

st.set_page_config(layout="wide")

movies=joblib.load('movie_list1.joblib')
similarity=joblib.load('similarity1.joblib')
movies_list=movies['Movie_Title'].values


st.title('**🎬 Movie Recommendation System**')
st.write("**Welcome to our movie recommendation system! Select a movie from the dropdown list, and we'll recommend similar movies for you.**")



selected_movies=st.selectbox('**Select a Movie**',movies_list)


def recommendation(movie):
    index=movies[movies['Movie_Title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommeded_movies=[]
    for i in distance[1:6]:
        recommeded_movies.append(movies.iloc[i[0]].Movie_Title)
    return recommeded_movies

if st.button('**show recommed**'):
    movie_name=recommendation(selected_movies)
    st.write("**Recommended Movies:**")
    for i, movie in enumerate(movie_name, start=1):
        st.write(f"{i}. {movie}")

