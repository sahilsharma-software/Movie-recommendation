import streamlit as st
from joblib import load
from utils.helper import fetch_poster
import requests

# ------------------ CONFIG ------------------

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ------------------ LOAD DATA ------------------

@st.cache_data
def load_data():
    movies = load('models/movies.joblib')
    similarity = load('models/similarity.joblib')
    return movies, similarity

movies, similarity = load_data()
#----------------fetch from api---------------
def fetch_from_api(movie):
    url = f"http://localhost:8000/recommend/{movie}"
    response = requests.get(url)
    return response.json()["movies"]


# ------------------ RECOMMEND FUNCTION ------------------
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title

        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ------------------ UI ------------------

st.title("🎬 Movie Recommendation System")
st.markdown("Get similar movies with posters 🍿")

selected_movie = st.selectbox(
"🔍 Choose a movie:",
movies['title'].values
)

# ------------------ BUTTON ------------------
if st.button("🚀 Recommend"):
    with st.spinner("Finding best movies for you... 🍿"):
        results = fetch_from_api(selected_movie)

        names = []
        posters = []

        for item in results:
            names.append(item['title'])
            posters.append(fetch_poster(item['movie_id']))

    if not names:
        st.error("Movie not found!")
    else:
        st.subheader("🎯 Recommended Movies")

        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.image(posters[i])
                st.markdown(f"**{names[i]}**")