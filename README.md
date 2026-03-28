# 🎬 Movie Recommendation System (Dockerized Full Stack ML App)

A full-stack Movie Recommendation System built using **Machine Learning**, **FastAPI**, **Streamlit**, and **Docker**.
This project suggests similar movies based on user selection and displays posters using an external API.

---

## 🚀 Features

* 🎯 Content-based movie recommendation system
* ⚡ FastAPI backend for high-performance API
* 🎨 Interactive Streamlit frontend
* 🐳 Fully Dockerized (run anywhere easily)
* 📦 Clean and modular code structure

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (Frontend)
* **FastAPI** (Backend API)
* **Scikit-learn** (ML Model)
* **Pandas / NumPy**
* **Docker**

---

## 📂 Project Structure

```
Movie_recommendation/
│
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── Dockerfile              # Docker configuration
├── requirements.txt        # Dependencies
├── utils/
│   └── helper.py           # Helper functions (poster fetch etc.)
├── notebook/
│   └── Movies_recommendation.ipynb
├── models/                 # (Not included - download separately)
└── .gitignore
```

---

## ⚙️ Installation (Without Docker)

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender

pip install -r requirements.txt

# Run FastAPI
uvicorn main:app --reload

# Run Streamlit (new terminal)
streamlit run app.py
```

---

## 🐳 Run with Docker (Recommended)

```bash
# Build image
docker build -t movie-recommender .

# Run container
docker run -p 8501:8501 -p 8000:8000 movie-recommender
```

---

## 🌐 Access the App

* 🎨 Streamlit UI → http://localhost:8501
* ⚡ FastAPI → http://localhost:8000
* 📄 API Docs → http://localhost:8000/docs

---

## 📊 How it Works

1. User selects a movie from Streamlit UI
2. Request sent to FastAPI backend
3. Backend computes similarity using ML model
4. Returns top 5 recommended movies
5. Posters fetched and displayed

---

## ⚠️ Note

* `models/` folder is not included in this repository due to size limitations
* You need to generate or download the trained model files (`.joblib`) separately

---

## 📌 Future Improvements

* 🔍 Add search functionality
* 🌐 Deploy on cloud (Render / Railway)
* ❤️ Add user-based recommendations
* 📱 Improve UI/UX

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📧 Contact

**Sahil Sharma**
📌 Aspiring AI Engineer
🚀 Passionate about ML & Full Stack Development

---

⭐ If you like this project, don't forget to give it a star!
