import pandas as pd
import streamlit as st
import pickle

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:6]
    #but here we lose the index of the movie while sorting, so we have somehow keep the index to recommend the movie
    #key = lambda x:x[1] so that sorting takes palce due to the similarity and not index

    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
        #fetching movie poster
        #8265bd1679663a7ea12ac168da84d2e
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')




#to create webpage run in terminal : streamlit run app.py

import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button("Recommend"):
    recommedation = recommend(option)
    for i in recommedation:
        st.write(i)