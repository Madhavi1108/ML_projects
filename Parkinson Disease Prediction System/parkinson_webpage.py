import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Parkinson's Disease Predictor", layout="wide", page_icon="🧑‍⚕️")

# Load the model
parkinsons_model = pickle.load(open('parkinson_model.pkl', 'rb'))

# Title
st.title("🧠 Parkinson's Disease Prediction using ML")

st.markdown("Enter the following biomedical voice measurements to predict whether a person has Parkinson's disease.")

# Input fields
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    fo = st.text_input('MDVP:Fo(Hz)', '0')

with col2:
    fhi = st.text_input('MDVP:Fhi(Hz)', '0')

with col3:
    flo = st.text_input('MDVP:Flo(Hz)', '0')

with col4:
    Jitter_percent = st.text_input('MDVP:Jitter(%)', '0')

with col5:
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '0')

with col1:
    RAP = st.text_input('MDVP:RAP', '0')

with col2:
    PPQ = st.text_input('MDVP:PPQ', '0')

with col3:
    DDP = st.text_input('Jitter:DDP', '0')

with col4:
    Shimmer = st.text_input('MDVP:Shimmer', '0')

with col5:
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '0')

with col1:
    APQ3 = st.text_input('Shimmer:APQ3', '0')

with col2:
    APQ5 = st.text_input('Shimmer:APQ5', '0')

with col3:
    APQ = st.text_input('MDVP:APQ', '0')

with col4:
    DDA = st.text_input('Shimmer:DDA', '0')

with col5:
    NHR = st.text_input('NHR', '0')

with col1:
    HNR = st.text_input('HNR', '0')

with col2:
    RPDE = st.text_input('RPDE', '0')

with col3:
    DFA = st.text_input('DFA', '0')

with col4:
    spread1 = st.text_input('spread1', '0')

with col5:
    spread2 = st.text_input('spread2', '0')

with col1:
    D2 = st.text_input('D2', '0')

with col2:
    PPE = st.text_input('PPE', '0')

# Predict button
if st.button("🔍 Get Parkinson's Test Result"):
    try:
        user_input = [float(i) for i in [
            fo, fhi, flo, Jitter_percent, Jitter_Abs,
            RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
            APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]]
        result = parkinsons_model.predict([user_input])

        if result[0] == 1:
            st.error("❌ The person **has** Parkinson's disease.")
        else:
            st.success("✅ The person **does not have** Parkinson's disease.")

    except ValueError:
        st.warning("⚠️ Please make sure all fields are filled with valid numbers.")
