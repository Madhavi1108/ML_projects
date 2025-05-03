import streamlit as st
import pickle
# Data preprocessing
import nltk
from nltk.corpus import stopwords
import string

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

#Pre processing the data
st.title("Email/SMS Spam Classifier")
input_msg = st.text_input("Enter the message")

transformed_sms = transform_text(input_msg)

#Vectorizing the data
vector_input = tfidf.transform([transformed_sms])

#Predicting the model
result = model.predict(vector_input)[0]

#Displaying whether the msg is ham or spam
if result == 1:
    st.header("Spam")
else:
    st.header("Not Spam")
