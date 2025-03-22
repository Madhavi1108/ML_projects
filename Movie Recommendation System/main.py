import pandas as pd
import streamlit as st
import pickle

# Load the pickled data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Ensure this file exists

# Function to get movie recommendations with posters
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommendations.append(movie_title)
    return recommendations

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a Movie', movies['title'].values)

if st.button('Recommend'):
    recommended_movies= recommend(selected_movie_name)

    cols = st.columns(5)  # Display 5 movies side by side
    for i in range(5):
        with cols[i]:
            st.text(recommended_movies[i])
