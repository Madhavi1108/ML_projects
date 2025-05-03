import streamlit as st
import pandas as pd
import pickle

# Load saved data
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert back to DataFrame
books_df = pd.DataFrame(books)

# Function to fetch book recommendations
def recommend(book_name):
    if book_name not in books_df['Book-Title'].values:
        return ["Book not found"], ["https://via.placeholder.com/150"]

    book_index = books_df[books_df['Book-Title'] == book_name].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    images = []

    for i in books_list:
        recommendations.append(books_df.iloc[i[0]]['Book-Title'])
        images.append(books_df.iloc[i[0]]['Image-URL-L'])  # Adjust for correct image column

    return recommendations, images

# Streamlit UI
st.title('Book Recommendation System')

selected_book = st.selectbox('Select a Book', books_df['Book-Title'].values)

if st.button('Recommend'):
    recommended_books, book_images = recommend(selected_book)

    cols = st.columns(5)  # Display 5 books side by side
    for i in range(5):
        with cols[i]:
            st.image(book_images[i], use_container_width=True)
            st.text(recommended_books[i])
