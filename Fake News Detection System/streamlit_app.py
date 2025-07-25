import streamlit as st
import joblib
import pandas as pd
import re
import string

# --- Function: Text Preprocessing (same as wordopt) ---
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# --- Function: Output Label ---
def output_label(n):
    return "Fake News" if n == 0 else "Real News"

# --- Load models and vectorizer ---
LR = joblib.load("lr_model.pkl")
DT = joblib.load("dt_model.pkl")
GB = joblib.load("gb_model.pkl")
RF = joblib.load("rf_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# --- Streamlit UI ---
st.title("📰 Fake News Detector")
news_input = st.text_area("Enter the News Content Below:")

if st.button("Predict"):
    if news_input:
        cleaned = clean_text(news_input)
        vect_input = vectorizer.transform([cleaned])

        pred_lr = output_label(LR.predict(vect_input)[0])
        pred_dt = output_label(DT.predict(vect_input)[0])
        pred_gb = output_label(GB.predict(vect_input)[0])
        pred_rf = output_label(RF.predict(vect_input)[0])

        st.subheader("🔍 Predictions")
        st.write(f"**Logistic Regression:** {pred_lr}")
        st.write(f"**Decision Tree:** {pred_dt}")
        st.write(f"**Gradient Boosting:** {pred_gb}")
        st.write(f"**Random Forest:** {pred_rf}")
    else:
        st.warning("Please enter news content to predict.")
