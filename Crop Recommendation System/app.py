import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load scalers
with open("minmaxscaler.pkl", "rb") as file:
    minmax_scaler = pickle.load(file)

with open("standscaler.pkl", "rb") as file:
    stand_scaler = pickle.load(file)

# Crop Dictionary
crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
             8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
             14: "Pomegranate", 15: "Lentil", 16: "Black Gram", 17: "Mung Bean", 18: "Moth Beans",
             19: "Pigeon Peas", 20: "Kidney Beans", 21: "Chickpea", 22: "Coffee"}

# Streamlit UI
st.title("Crop Recommendation System")

# Input Fields
N = st.number_input("Nitrogen (N)", min_value=0, max_value=100, value=50)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=100, value=50)
K = st.number_input("Potassium (K)", min_value=0, max_value=100, value=50)
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=70.0)
ph = st.number_input("pH Level", value=6.5)
rainfall = st.number_input("Rainfall (mm)", value=200.0)

# Predict Button
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Apply MinMax Scaling first
    input_data = minmax_scaler.transform(input_data)

    # Apply Standard Scaling next
    input_data = stand_scaler.transform(input_data)

    prediction = model.predict(input_data)[0]  # Get predicted label

    if prediction in crop_dict:
        st.success(f"Recommended Crop: {crop_dict[prediction]}")
    else:
        st.error("Sorry, no suitable crop recommendation for this input.")
