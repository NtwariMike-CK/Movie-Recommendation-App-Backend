from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import pandas as pd
import numpy as np
import pickle
from dotenv import load_dotenv
import os
import requests
import gdown


# === Define the base path relative to the script ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# === Create models directory if it doesn't exist ===
os.makedirs(MODELS_DIR, exist_ok=True)

# === Google Drive file links ===
vectors_drive = "https://drive.google.com/uc?id=1B2yXv1mvsj86Tbmh3_zwG9C4LvIaMjnX"
similarity_drive = "https://drive.google.com/uc?id=1BqMwZTXQSLsr5Y-6gFIRjkTyGY0lTOUz"
data_drive = "https://drive.google.com/uc?id=1pwTW9svCRtAmqJxoWQjQ10_qWJBPXKEL"


# === Define local paths for each file ===
vectors_path = os.path.join(MODELS_DIR, "count_vecotirzer.pkl")
similarity_path = os.path.join(MODELS_DIR, "cosine_similarity_matrix.pkl")
data_path = os.path.join(MODELS_DIR, "cleaned_data.csv")

# === Download if not already present ===
if not os.path.exists(vectors_path):
    gdown.download(vectors_drive, vectors_path, quiet=False)

if not os.path.exists(similarity_path):
    gdown.download(similarity_drive, similarity_path, quiet=False)

if not os.path.exists(data_path):
    gdown.download(data_drive, data_path, quiet=False)




# Load environment variables from .env.local
load_dotenv(".env.local")
api_key = os.getenv("TMDB_API_KEY")
if not api_key:
  raise Exception("Api key invalid")

# Define all the urls
TMDB_URL = "https://api.themoviedb.org/3/movie/"
params = {
  "api_key": api_key,
  "language": "en-US"
}

# define the app
app = FastAPI()

# # Allow requests from your frontend
origins = [
    os.getenv("DEVEPLOPMENT_ORIGIN"),  # React dev server
    os.getenv("FULL_DEVEPLOPMENT_HOME"),  # Some systems use 127.0.0.1 instead of localhost
    os.getenv("FRONTEND_ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed origins
    # allow_origins=["*"]  #Allow this if your api is free to be used by the public
    allow_credentials=True,
    allow_methods=["*"],              # Allow all methods (GET, POST, etc)
    allow_headers=["*"],              # Allow all headers
)


# Let's get our datasets
movies = pd.read_csv("./models/cleaned_data.csv")


# Let's get our models defined
with open("./models/count_vecotirzer.pkl", "rb") as f:
  vectors = pickle.load(f)
with open("./models/cosine_similarity_matrix.pkl", "rb") as f:
  similarity = pickle.load(f)


# NORMAL FUNCTIONS HERE-------------------------------------------
IMAGE_PATH = "https://image.tmdb.org/t/p/w500"
def online_movies(recommendations: list):
  fetch_results = []
  for movie in recommendations:
    # full_url = TMDB_URL + movie + "?" + "api_key=" + api_key + "&" + params
    full_url = TMDB_URL + str(movie)
    response = requests.get(full_url, params)
    response.raise_for_status()  # Raise exception for non-200 responses
    data = response.json()

    # Add any additional data you want to include
    enhanced_movie = {
        "id": data.get("id"),
        "title": data.get("title"),
        "poster_path": IMAGE_PATH + data.get("poster_path"),
        "overview": data.get("overview"),
        "release_date": data.get("release_date"),
        "vote_average": data.get("vote_average"),
        "genres": [genre.get("name") for genre in data.get("genres", [])]
    }
    fetch_results.append(enhanced_movie)
  return fetch_results


# APIS ROUTES HERE -----------------------------------------------
# Define the root api
@app.get("/")
def home():
  return {"message": "Hello, welcome to movie recommendation system"}


# define paths to retrieve movie data
@app.get("/movies")
def get_movies():
  return movies[["title", "movie_id"]].to_dict(orient="records")


#Get recommendations from a particular movie
@app.get("/recommendations/{movie_id}", response_model=List[Dict[str, Any]])
def get_recommendations(movie_id: int):
  # First check if the movie_id exists in our dataset
  if movie_id not in movies["movie_id"].values:
    raise HTTPException(status_code=404, detail=f"Movie ID {movie_id} not found in our database")

  try:
    #Find the movie in our dataset
    movie_index = movies[movies['movie_id'] == movie_id].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    top_20 = movie_list[:21]

    # Get recommendations
    all_indexes = []
    for i in top_20:
      all_indexes.append(movies.iloc[i[0]]["movie_id"])

    results = online_movies(all_indexes)
    return results
    
  except IndexError:
      raise HTTPException(status_code=404, detail=f"Movie ID {movie_id} exists but cannot generate recommendations for it")
  except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")
