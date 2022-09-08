import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=API KEY'.format(movie_id))
    data = response.json()
    try:
        return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    except:
        pass


def recommend(movie):
    movies_list = sorted(list(enumerate(similarity[movies[movies['title'] == movie].index[0]])), reverse=True, key=lambda x: x[1])[1: 6]
    recommended_movies = [movies.iloc[j[0]].title for j in movies_list]
    recommended_posters = [fetch_poster(movies.iloc[j[0]].movie_id) for j in movies_list]
    return recommended_movies, recommended_posters


movies = pd.DataFrame(pickle.load(open('movie_list.pkl', 'rb')))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.write('Indraneel Dey')
st.write('Indian Institute of Technology, Madras')
st.title('Movie Recommendation System')
selected_movie = st.selectbox('Type or select the movie you like', movies['title'].values)

if st.button('Recommend'):
    col = [0, 0, 0, 0, 0]
    col[0], col[1], col[2], col[3], col[4] = st.columns(5)
    names, posters = recommend(selected_movie)
    for i in range(5):
        with col[i]:
            st.text(names[i])
            try:
                st.image(posters[i])
            except:
                pass
