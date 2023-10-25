import pickle
import streamlit as st
import requests


movie_credits = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=75eb0685f1f9140663e33eb0ea57150a"
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommender(movie_name):

    movie_index = movie_credits[movie_credits["title"] == movie_name].index[0]
    distnaces = similarity[movie_index]
    index_list = list(enumerate(distnaces))
    similar_movie = sorted(index_list, reverse=True, key = lambda x: x[1])[0:10]
    
    similar_movie_titles = []
    similar_movie_posters = []
    
    for i in similar_movie:
        
        movie_id = movie_credits.iloc[i[0],0]
        similar_movie_titles.append(movie_credits.iloc[i[0],1])
        similar_movie_posters.append(fetch_poster(movie_id))
        
    return similar_movie_titles, similar_movie_posters

  
st.header('Content Based Film Recommendation System')


movie_list = movie_credits['title'].values
selected_movie = st.selectbox(
    "Input the name of a movie or choose one from the provided list",
    movie_list
)


if st.button('Search'):
    recommended_movie_names,recommended_movie_posters = recommender(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])
        

    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])
        
    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])
        
    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])

        
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie_names[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie_names[6])
        

    with col3:
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie_names[7])
        
    with col4:
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie_names[8])
        
    with col5:
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie_names[9])
   