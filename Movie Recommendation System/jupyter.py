import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load datasets
movies = pd.read_csv(r"C:\Users\Madhavi\Downloads\archive\tmdb_5000_movies.csv")
credits = pd.read_csv(r"C:\Users\Madhavi\Downloads\archive\tmdb_5000_credits.csv")

# Merge datasets on title
movies = movies.merge(credits, on='title')

# Select relevant columns
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Remove null values & duplicates
movies.dropna(inplace=True)
movies.drop_duplicates(inplace=True)

# Function to safely convert JSON-like strings to lists
def convert(obj):
    try:
        data = ast.literal_eval(obj)  # Safely evaluate the string
        return [i['name'] for i in data if isinstance(i, dict) and 'name' in i] if isinstance(data, list) else []
    except (ValueError, SyntaxError):  
        return []

# Extract first 3 cast members
def convert2(obj):
    try:
        return [i['name'] for i in ast.literal_eval(obj)[:3]]  # Use list slicing
    except (ValueError, SyntaxError):
        return []

  # Fetch director information
def fetch_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i.get('job') == 'Director':
                return [i['name']]  # Return as list
        return []
    except (ValueError, SyntaxError):
        return []

  # Apply conversion to relevant columns
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert2)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())  # Already returns a list

# Removing spaces inside names (e.g., "Sam Worthington" → "SamWorthington")
movies['genres'] = movies['genres'].apply(lambda x: ["".join(i.split()) for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: ["".join(i.split()) for i in x])
movies['cast'] = movies['cast'].apply(lambda x: ["".join(i.split()) for i in x])
movies['crew'] = movies['crew'].apply(lambda x: ["".join(i.split()) for i in x])

# Create 'tags' column by concatenating processed data
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Create new dataframe with selected columns
new_df = movies[['movie_id', 'title', 'tags']].copy()

# Convert list to string and apply lowercase more efficiently
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(map(str.lower, x)))

# Display first few rows
#new_df.head()

cv = CountVectorizer(max_features=5000, stop_words='english')

# Transform tags into vectors
vectors = cv.fit_transform(new_df['tags']).toarray()

# Using stemming
ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(i) for i in text.split()])

# Apply stemming
new_df['tags'] = new_df['tags'].apply(stem) 

similarity = cosine_similarity(vectors)

def recommend_movie(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

pickle.dump(new_df,open('movies.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))
pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb'))
