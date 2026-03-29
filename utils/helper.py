import requests
import streamlit as st

def fetch_poster(movie_id):
    try:
        API_KEY = st.secrets["API_KEY"]

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"