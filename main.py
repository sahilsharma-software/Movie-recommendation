from fastapi import FastAPI
from joblib import load

app = FastAPI()

# ------------------ LOAD DATA ------------------
movies = load('models/movies.joblib')
similarity = load('models/similarity.joblib')

# ------------------ HOME ------------------
@app.get("/")
def home():
    return {"message": "Movie Recommender API is running 🚀"}

# ------------------ RECOMMEND API ------------------
@app.get("/recommend/{movie}")
def recommend(movie: str):
    if movie not in movies['title'].values:
        return {"movies": []}

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append({
            "title": title,
            "movie_id": int(movie_id)
        })

    return {"movies": recommended_movies}