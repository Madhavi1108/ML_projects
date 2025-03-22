import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
ratings = pd.read_csv("Ratings.csv")
books = pd.read_csv("Books.csv")
users = pd.read_csv("Users.csv")

# Step 1: Select top 50 books based on number of ratings
top_books = ratings['ISBN'].value_counts().head(50).index  # Get top 50 books by ISBN
filtered_books = books[books['ISBN'].isin(top_books)].copy()

# Step 2: Data Cleaning
filtered_books = filtered_books.dropna().drop_duplicates()
filtered_books.loc[:, 'Year-Of-Publication'] = filtered_books['Year-Of-Publication'].astype(str)

# Step 3: Create a 'tags' column for content similarity
filtered_books.loc[:, 'tags'] = (filtered_books['Book-Title'] + " " +
                                 filtered_books['Book-Author'] + " " +
                                 filtered_books['Publisher'] + " " +
                                 filtered_books['Year-Of-Publication']).str.lower()

# Step 4: Convert tags to numerical vectors for similarity calculation
cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(filtered_books['tags'])

# Step 5: Compute similarity matrix
similarity = cosine_similarity(vectors)

# Step 6: Save processed data
pickle.dump(filtered_books, open("books.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("✅ Processed and saved top 50 books with similarity matrix!")
