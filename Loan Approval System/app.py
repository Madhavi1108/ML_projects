import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏦 Loan Approval Prediction System")
st.markdown("Fill in the details to check if the loan would be approved.")

# Input fields
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0)
LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0.0)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0.0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert inputs to numeric
gender = 1 if Gender == "Male" else 0
married = 1 if Married == "Yes" else 0
dependents = 3 if Dependents == "3+" else int(Dependents)
education = 0 if Education == "Graduate" else 1
self_employed = 1 if Self_Employed == "Yes" else 0

# Encode Property Area as a single feature (one value)
if Property_Area == "Urban":
    property_area = 2
elif Property_Area == "Semiurban":
    property_area = 1
else:  # Rural
    property_area = 0

# Create the final input vector (must match training order and count)
input_data = np.array([
    gender, married, dependents, education, self_employed,
    ApplicantIncome, CoapplicantIncome, LoanAmount,
    Loan_Amount_Term, Credit_History, property_area
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
