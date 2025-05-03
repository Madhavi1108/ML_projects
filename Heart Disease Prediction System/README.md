**Heart Disease Prediction Project**

**Overview**

This project consists of a Python-based machine learning model for predicting heart disease and a Streamlit web application for user interaction.  The model is trained on a dataset of heart-related health information, and the web app provides a user-friendly interface to input patient data and receive a prediction.

**Files**

* **`heart_disease.ipynb`**:  This Jupyter Notebook contains the Python code for:
    * Data loading and preprocessing using Pandas and NumPy.
    * Splitting the data into training and testing sets using scikit-learn.
    * Training a Logistic Regression model to predict heart disease.
    * Evaluating the model's accuracy.
    * Saving the trained model and StandardScaler using the `pickle` library.
* **`heart_webpage_page.py`**:  This Python script uses the Streamlit library to create a web application.  The application:
    * Loads the saved Logistic Regression model and StandardScaler.
    * Provides input fields for users to enter patient data (age, sex, chest pain type, blood pressure, cholesterol, etc.).
    * Uses the loaded model to predict the likelihood of heart disease based on the user's input.
    * Displays the prediction result to the user.

**Data**

The project uses a dataset (`heart.csv`) with the following features:

* age
* sex (1 = male; 0 = female)
* cp (chest pain type)
* trestbps (resting blood pressure)
* chol (serum cholesterol)
* fbs (fasting blood sugar > 120 mg/dl)
* restecg (resting electrocardiographic results)
* thalach (maximum heart rate achieved)
* exang (exercise-induced angina)
* oldpeak (ST depression induced by exercise relative to rest)
* slope (the slope of the peak exercise ST segment)
* ca (number of major vessels)
* thal (thalassemia)
* target (presence of heart disease)

**Dependencies**

* Python 3.x
* Pandas
* NumPy
* scikit-learn
* Streamlit
* pickle

**How to Use**

1.  **Notebook (`heart_disease.ipynb`)**
    * Ensure you have Jupyter Notebook or JupyterLab installed.
    * Open and run the notebook.  You'll need to upload the `heart.csv` data file when prompted.
    * The notebook will train the model and save `heart_model.sav` and `heart_scaler.sav`.

2.  **Web Application (`heart_webpage_page.py`)**
    * Make sure you have Streamlit installed (`pip install streamlit`).
    * Place the `heart_webpage_page.py`, `heart_model.sav`, and `heart_scaler.sav` in the same directory.
    * Run the script from the command line:  `streamlit run heart_webpage_page.py`
    * Streamlit will open the web application in your browser.
    * Enter the patient's information in the input fields and click the prediction button.

**Important Notes**

* This project is for informational purposes only and should not be used as a substitute for professional medical advice.
* The accuracy of the prediction depends on the quality and representativeness of the training data.