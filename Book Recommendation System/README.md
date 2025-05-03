# Book Recommendation System

## Overview
This is a content-based Book Recommendation System that suggests books similar to a selected one. The system uses text-based features like book title, author, publisher, and publication year to compute similarity between books using the CountVectorizer and cosine similarity.

## Features
- Processes and filters the top 50 books based on user ratings.
- Cleans and prepares the dataset for similarity computation.
- Uses Natural Language Processing (NLP) techniques to convert book metadata into feature vectors.
- Computes cosine similarity between books.
- Provides book recommendations with corresponding cover images using a Streamlit UI.

## Dataset Used
- **Ratings.csv**: Contains user ratings for books.
- **Books.csv**: Contains book details (ISBN, Title, Author, Publisher, Year of Publication, etc.).
- **Users.csv**: Contains user demographic information.

## Installation
1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```sh
   pip install numpy pandas scikit-learn streamlit
   ```
3. Ensure the dataset files (Ratings.csv, Books.csv, Users.csv) are in the project directory.

## Data Processing
Run the following script to process the dataset and generate similarity data:
```sh
python preprocess.py
```
This will:
- Filter the top 50 books based on the number of ratings.
- Clean the dataset and create a feature-based "tags" column.
- Compute the cosine similarity matrix.
- Save the processed data as `books.pkl` and `similarity.pkl` using pickle.

## Running the Streamlit App
To launch the recommendation system UI, run:
```sh
streamlit run app.py
```
This will open a web interface where you can select a book and receive recommendations.

## Usage
1. Open the Streamlit app.
2. Select a book from the dropdown menu.
3. Click the "Recommend" button.
4. View the recommended books with their cover images.

## Project Structure
```
├── preprocess.py  # Script to process and generate similarity data
├── app.py         # Streamlit UI for book recommendations
├── books.pkl      # Processed book data
├── similarity.pkl # Cosine similarity matrix
├── Ratings.csv    # Ratings dataset
├── Books.csv      # Books dataset
├── Users.csv      # Users dataset
└── README.md      # Project documentation
```

## Future Improvements
- Expand dataset to include more books.
- Incorporate user-based collaborative filtering.
- Improve UI with more details and interactivity.
- Implement genre-based filtering.
