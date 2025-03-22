import numpy as np
import pickle
import streamlit as st

# Load trained model and scaler
loaded_model = pickle.load(open("trained_model (1).sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))  # Load the fitted scaler

def diabetes_prediction(input_data):
    # Convert input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float).reshape(1, -1)

    # Standardize input using the loaded scaler
    std_data = scaler.transform(input_data_as_numpy_array)

    # Perform prediction
    prediction = loaded_model.predict(std_data)

    # Return result
    return "The person is not diabetic" if prediction[0] == 0 else "The person is diabetic"

def main():
    st.title("Diabetes Prediction Web App")

    # Getting input data from user
    pregnancies = st.text_input('Number of Pregnancies')
    glucose = st.text_input('Glucose Level')
    blood_pressure = st.text_input('Blood Pressure value')
    skin_thickness = st.text_input('Skin Thickness Value')
    insulin = st.text_input('Insulin Level')
    bmi = st.text_input('BMI Value')
    diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function Value')
    age = st.text_input('Age of the Person')

    diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float
            input_values = [
                float(pregnancies), float(glucose), float(blood_pressure),
                float(skin_thickness), float(insulin), float(bmi),
                float(diabetes_pedigree_function), float(age)
            ]
            diagnosis = diabetes_prediction(input_values)
        except ValueError:
            diagnosis = "Invalid input! Please enter numeric values."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
