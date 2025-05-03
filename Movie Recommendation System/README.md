# Movie-recommendation-system (Data handling using Jupyter notebook)

## Overview
This project implements a **Content-Based Movie Recommendation System** using **Natural Language Processing (NLP)** and **Machine Learning** techniques. It processes movie metadata, extracts meaningful features, and computes similarity scores to suggest movies based on user preferences.

## Features
- Uses **TF-IDF Vectorization** for feature extraction.
- Applies **stemming** to reduce words to their root form.
- Computes **cosine similarity** to find the most similar movies.
- Extracts movie details such as **genres, keywords, cast, and director**.
- Saves the processed data as pickle files for efficient use in a web application.

## Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **NLTK**
- **Pickle**

## Dataset
This project uses the **TMDb 5000 Movies Dataset**, which contains metadata about movies such as genres, cast, crew, and keywords.

## Installation
### Prerequisites
Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

### Install Required Libraries
Run the following command to install the necessary dependencies:
```bash
pip install numpy pandas scikit-learn nltk
```

## Usage
### 1. Load and Process the Dataset
- The script loads two CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`).
- Merges them on the `title` column.
- Extracts relevant columns (`movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`).
- Converts JSON-like strings into lists.
- Removes spaces in names for consistency.
- Creates a **'tags'** column containing combined features.

### 2. Feature Extraction
- Uses **CountVectorizer** to convert text data into numerical vectors (Bag of Words model).
- Applies **stemming** to normalize words.
- Computes **cosine similarity** between movie vectors.

### 3. Movie Recommendation
To get recommendations, use:
```python
recommend_movie("Movie Name")
```
This will print the top 5 recommended movies.

### 4. Save Processed Data
The processed data is saved as **pickle files**:
- `movies.pkl` – Processed DataFrame.
- `similarity.pkl` – Cosine similarity matrix.
- `movies_dict.pkl` – Dictionary format for easy loading in applications.

## Future Enhancements
- Implement a **web interface** using **Streamlit**.
- Fetch **movie posters** using web scraping.
- Include user-based collaborative filtering.

# Movie Recommender System Interface in Pycharm

## Overview
This project is a **Movie Recommender System** built using **Python**, **Streamlit**, and **Pickle** for data storage. The application suggests movies based on user selection using a similarity matrix computed from movie metadata.

## Features
- Users can **select a movie** from a dropdown menu.
- The system **recommends 5 similar movies** based on cosine similarity.
- Built with **Streamlit** for an interactive UI.
- Uses **pickled preprocessed data** for efficiency.

## Installation
### 1. Install Python
Ensure that Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### 2. Install Required Libraries
Run the following command to install dependencies:
```sh
pip install pandas streamlit pickle5
```

### 3. Run the Application
Navigate to the project folder and execute:
```sh
streamlit run app.py
```

## File Structure
```
Movie-Recommender/
│── app.py                # Streamlit app
│── movies_dict.pkl       # Pickled movie dataset
│── similarity.pkl        # Pickled similarity matrix
│── README.md             # Project documentation
```

## Usage
1. **Run the application** using `streamlit run app.py`.
2. **Select a movie** from the dropdown menu.
3. **View recommended movies** displayed in a side-by-side format.

## Code Explanation
### app.py
- **Load Data**: The movie dataset and similarity matrix are loaded from `.pkl` files.
- **Recommendation Logic**: The system finds the most similar movies using cosine similarity.
- **UI Implementation**: Streamlit is used for an interactive user interface.

### Recommendation Algorithm
1. Finds the selected movie's index.
2. Retrieves similarity scores from the precomputed matrix.
3. Sorts and selects the top 5 similar movies.

## Future Improvements
- Enhance recommendations using **advanced NLP techniques**.
- **Web scraping** to fetch movie posters.
- Add **user-based recommendations**.

## License
This project is for educational purposes. Feel free to modify and enhance it!
