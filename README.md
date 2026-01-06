🎬 Movie Recommendation System

A simple content-based movie recommendation system built using Machine Learning and Streamlit.
Enter any movie name and get 5 similar movie recommendations along with their poster images.

🧪 Demo

👉 Live App: Open in Streamlit

The user interface displays 5 recommended movies with their posters in a clean and responsive layout.

🚀 Features

🎯 Content-based filtering using Cosine Similarity

🖼️ Movie poster fetching using TMDB API

⚡ Fast loading with parallel API calls

📱 Responsive and simple UI built with Streamlit

📁 Project Structure
├── Movie_Recommendation_Sysem.ipynb   # Data cleaning, feature extraction & model creation
├── app.py                             # Streamlit application
├── movies_df.pkl                      # Preprocessed movie dataset (generated)
├── similarity.pkl                     # Cosine similarity matrix (generated)
├── tmdb_5000_movies.csv               # Original TMDB dataset
├── tmdb_5000_credits.csv              # Original TMDB credits dataset
├── requirements.txt                   # Required Python libraries
└── README.md

🛠 Tech Stack
Tool / Library	Purpose
Python	Programming language
Streamlit	Web application UI
Scikit-learn	Similarity calculation
Pandas	Data manipulation & handling
TMDB API	Movie poster retrieval
🌐 TMDB API

Movie posters are fetched using The Movie Database (TMDB) API.

🔑 Generate your API key here:
👉 https://www.themoviedb.org/settings/api

In app.py, replace the API key:

API_KEY = "your_api_key_here"

📦 Data & Pickle Files

This project requires the following pickle files, which are not included in the repository:

movies_df.pkl

similarity.pkl

How to Generate Them

Download the dataset from Kaggle:
👉 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Run the notebook:

Movie_Recommendation_Sysem.ipynb


Generate pickle files using:

import pickle

pickle.dump(movies_df, open('movies_df.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

▶️ Run the Application Locally
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run Streamlit App
streamlit run app.py

📌 Output

Enter a movie name

Get 5 similar movie recommendations

View poster images fetched dynamically from TMDB
