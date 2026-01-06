import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
songs = pd.read_csv("songs.csv")

# Step 1: Create a 'features' column by combining writer and genre
songs["features"] = songs["writer"] + " " + songs["genre"]

# Step 2: Convert text to vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(songs["features"])

# Step 3: Calculate similarity matrix
similarity = cosine_similarity(feature_vectors)

# Streamlit UI
st.title("🎧 AI Music Recommender (with Scikit-learn)")
selected_song = st.selectbox("Choose a song:", songs["song"])

# Get index of selected song
song_index = songs[songs["song"] == selected_song].index[0]

# Get similarity scores
similar_songs = list(enumerate(similarity[song_index]))

# Sort songs by similarity score (excluding itself)
sorted_songs = sorted(similar_songs, key=lambda x: x[1], reverse=True)[1:6]

# Show results
st.subheader("🎶 Because you liked this song, you may also like:")
for idx, score in sorted_songs:
    st.write(f"- {songs.iloc[idx]['song']} (Writer: {songs.iloc[idx]['writer']}, Genre: {songs.iloc[idx]['genre']})")
