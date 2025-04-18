# Movie Recommendation System Using Machine Learning

A web application that recommends movies based on user selection using machine learning algorithms. The system features a stylish interface with Greek-inspired typography and a responsive design.


## Features

- **Movie Search and Selection**: Search for movies through an interactive dropdown that supports real-time filtering
- **Alphabetical Sorting**: Movies displayed in alphabetical order for easy navigation
- **Machine Learning Recommendations**: Get movie recommendations similar to your selected movie using a trained ML model
- **Responsive Design**: Works seamlessly across different device sizes
- **Horizontal Scrolling Movie Display**: Navigate through recommended movies with an intuitive left-right scrolling interface

## Technology Stack

- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Backend**: API endpoint that serves movie data and recommendations using FastAPI
- **Machine Learning**: Recommendation algorithms (details can be specified based on your actual implementation)

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm or yarn package manager
- FastApi
- Dotenv
- 
- Backend API endpoint (configured in environment variables)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Create a `.env.local` file in the root directory and add your backend URL:
   ```
   NEXT_PUBLIC_BACKEND_URL=https://your-api-endpoint.com
   ```

4. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## Project Structure

```
movie-recommendation-system/
├── components/
│   └── recommendemovies.tsx    # Movie section component with horizontal scrolling
├── pages/
│   └── index.tsx               # Home page with movie selection and recommendations
├── styles/
│   └── scrollbar.css           # Custom scrollbar styling
├── public/
│   └── assets/                 # Static assets
├── .env.local                  # Environment variables (not tracked in git)
├── package.json
└── README.md
```

## Usage

1. Open the application in your web browser
2. Click on the dropdown menu to select a movie or start typing to search
3. Choose a movie from the list
4. Click the "Προτάσεις Ταινιών" (Movie Recommendations) button
5. Browse through the horizontally scrollable list of recommended movies

## Frontend Component Details

### Home Page (index.tsx)

The main page features:
- Greek-inspired typography with imported Google Fonts
- Interactive movie selection dropdown with search functionality
- Movie recommendations display section
- Click-outside detection to close the dropdown when clicking elsewhere

### Movie Section Component (recommendemovies.tsx)

This component handles:
- Horizontal scrolling movie display with fixed-size movie cards
- Navigation buttons for scrolling left and right
- Consistent styling for movie posters and titles
- Fallback display for missing images

## Backend Component Details

### Movie Recommendation System

This part creates a recommendation system that uses content based filtering system where
since it is the better option for the movies

- 

## Customization

### Styling

The application uses Tailwind CSS for styling. You can customize the appearance by modifying the classes in the components.


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