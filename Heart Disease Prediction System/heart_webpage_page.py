import numpy as np
import pickle
import streamlit as st

# Load saved model and scaler
model = pickle.load(open("heart_model.sav", "rb"))
scaler = pickle.load(open("heart_scaler.sav", "rb"))

def heart_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return "No Heart Disease" if prediction[0] == 0 else "Heart Disease Detected"

def main():
    st.title("Heart Disease Prediction Web App")

    age = st.text_input("Age")
    sex = st.text_input("Sex (1 = male; 0 = female)")
    cp = st.text_input("Chest Pain Type (0–3)")
    trestbps = st.text_input("Resting Blood Pressure")
    chol = st.text_input("Serum Cholesterol (mg/dl)")
    fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
    restecg = st.text_input("Resting ECG results (0–2)")
    thalach = st.text_input("Max Heart Rate Achieved")
    exang = st.text_input("Exercise Induced Angina (1 = yes; 0 = no)")
    oldpeak = st.text_input("ST depression induced by exercise")
    slope = st.text_input("Slope of peak exercise ST segment (0–2)")
    ca = st.text_input("Number of major vessels (0–3)")
    thal = st.text_input("Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible)")

    diagnosis = ""
    if st.button("Heart Disease Test Result"):
        try:
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal]
            input_data = list(map(float, input_data))
            diagnosis = heart_prediction(input_data)
        except ValueError:
            diagnosis = "Invalid input! Please enter all fields as numbers."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
