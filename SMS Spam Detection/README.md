#  SMS/Email Spam Classifier  

## Description  

This project is a **machine learning-based spam detection system** that classifies SMS and email messages as **Spam** or **Not Spam**. It utilizes **Natural Language Processing (NLP)** techniques for text preprocessing and a **machine learning model** to make predictions. The web-based interface is built using **Streamlit**, allowing users to input messages and receive real-time classification results.  

##  Key Highlights  

- **Text Preprocessing**:  
  - Converts text to lowercase  
  - Tokenization  
  - Removes punctuation & stopwords  
  - Applies stemming using **Porter Stemmer**  
- **TF-IDF Vectorization**: Converts text into numerical features  
- **Machine Learning Model**: Pretrained classifier loaded from `model.pkl`  
- **Interactive UI**: Built with **Streamlit** for easy usability  

##  Objective  

The primary goal of this project is to provide an efficient and accurate **spam detection system** to filter out unwanted messages from SMS and emails, enhancing communication security.  

---

##  Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Madhavi1108/SMS-Spam-Detection-System.git
   cd SMS-Spam-Detection-System
   ```

2. Install dependencies:  
   ```bash
   pip install streamlit nltk scikit-learn pickle5
   ```

3. Download **NLTK Stopwords** (if running for the first time):  
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

---

## 🔧 Usage  

1. Run the **Streamlit app**:  
   ```bash
   streamlit run app.py
   ```
   
2. Enter a message in the input box and click Enter.  
3. The app will classify the message as **Spam** or **Not Spam**.  

---

##  Project Structure  

```
 SMS-Spam-Detection-System
│──  app.py               # Main Streamlit app
│──  model.pkl            # Trained Machine Learning model
│──  vectorizer.pkl       # TF-IDF vectorizer
│──  README.md            # Project documentation
│──  requirements.txt     # Required libraries
```
