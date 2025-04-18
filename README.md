# Movie Recommendation System Using Machine Learning

This is the backend of the Movie recommendation webApp that helps users see similar movies to their movie choice


## BACKEND Features

This backend is divided into two parts, the first one is Recommendation system and the second part is FastApi for restful apis

### 1. Recommendation System

I created a recommendation system based on content filtering as it is the best option in movie recommendation systems.

#### STEPS TAKEN:

- **Data Collection**: I used kaggle tmdb 500 movie datasets
- **Data Cleaning**: Ensured that the data is clean, has no duplicates, none values or missing fields etc.
- **Keyword generation**: Since I used content filtering, i had to create a column of tags to use for vectors and similarity
- **Text cleaning and vector generation**: I used nltk to create embeddings, remove stopwords, etc.
- **Similarity Score**: After cleaning everytrhing, i used cosine similarity to generate similarity between all movies

### 1. FastAPI and restful Apis creatiion

For this part we created the APIs that will be interacting with my frontend using FastApi
**Note:** The similarity scores and the movie dataset are stored on github, use gdown, os and pickle to download and use this app
locally

#### STEPS TAKEN:

- **Import All neccessary packages**: I imported all the packages and tools needed for this app [pickle, pandas, fastapi etc]
- **Load the dataset and the models**: Used gdown and pickle to load dataset and models from google drive into our working directory
- **Set frontend origins**: to make my apis secure, i defined the frontend apis for my app to listen to
- **Fetched Data from the tmdb**: For images, i fecthed data from the tmdb apis to display the images of the recommended movies
- **Set Api endpoints**: I set Api endpoints to be used in frontend (movies for all movies and recommendation for recommendations)

## Technology Stack

- **Recommendation system**: nltk, pandas, numpy, cosine similarity
- **API**: FastAPI, gdown, pickle, request

## Getting Started

### Prerequisites

- FastAPI
- pip / python
- Dotenv
- pickle
- gdown

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NtwariMike-CK/Movie-Recommendation-App-Backend.git
   cd movie-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install requirements.txt
   ```
3. Go to tmdb developer
- Create an account
- Generate a api_key


4. Create a `.env.local` file in the root directory and add your backend URL:
   ```
   TMDB_API_KEY = your_generated_api_key
   FRONTEND_ORIGIN=https://myapp.com
   DEVEPLOPMENT_ORIGIN=http://localhost:3000
   FULL_DEVEPLOPMENT_HOME=http://192.168.1.71:3000
   add more origins to be allowed to use your apis
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload >>
   ```

6. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## Project Structure

```
Movie-Recommendation-App-Backend/
├── backend/
│   └── models/
│     └── cleaned_movies.csv
│     └── vectors.pkl
│     └── similarity_score,pkl
│   └── .env.local
│   └── main.app
└── README.md
 
```

## Usage

1. Run your server uvicorn main:app --reload >>
2. run http://localhost:3000/movies to see all movies and their movie_id
3. run http://localhost:3000/recommendation/{movie_id} to see the list of recommended movies and their data

## Backend API Requirements

The application expects the backend API to provide:

1. A `/movies` endpoint that returns an array of movies with at least the following properties:
   ```json
   [
     {
       "id": 123,
       "title": "Movie Title"
     }
   ]
   ```

2. A `/recommendations/{movieId}` endpoint that returns an array of recommended movies:
   ```json
   [
     {
       "id": 456,
       "title": "Recommended Movie",
       "poster_path": "image_url_or_path",
       "overview": "Movie description",
       "release_date": "2023-01-01",
       "vote_average": 8.5
     }
   ]
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author
Ntwari Mike Chris Kevin

## Acknowledgments

- Movie data provided by TMDB
