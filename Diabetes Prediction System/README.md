# Diabetes Prediction System

This project consists of two main components:

1.  **Diabetes Prediction Model (diabetes_prediction.ipynb):**
    * This Jupyter Notebook contains the code for training a machine learning model to predict diabetes.
    * It uses the Support Vector Machine (SVM) algorithm for classification.
    * The notebook includes steps for:
        * Loading and preprocessing the diabetes dataset.
        * Splitting the data into training and testing sets.
        * Training the SVM model.
        * Evaluating the model's accuracy.
        * Saving the trained model and the StandardScaler used for feature scaling using pickle.

2.  **Diabetes Prediction Web Application (diabetes_webpage.py):**
    * This Python script creates a web application using the Streamlit library.
    * The web application allows users to input their health-related information (e.g., pregnancies, glucose level, blood pressure, etc.).
    * It loads the trained diabetes prediction model and the StandardScaler.
    * It uses the loaded model to predict whether the user is likely to have diabetes based on the input data.
    * The application displays the prediction result to the user.

##   Dependencies

* pandas
* numpy
* scikit-learn (sklearn)
* streamlit
* pickle

##   Usage

1.  **To run the Diabetes Prediction Model:**
    * Open and execute the `diabetes_prediction.ipynb` notebook in a Jupyter environment (e.g., Jupyter Notebook, JupyterLab, Google Colab).
    * Ensure that the `diabetes.csv` dataset is available or upload it when prompted.
    * The notebook will output the training and testing accuracy of the model and save the trained model (`trained_model.sav`) and the scaler (`scaler.sav`).

2.  **To run the Diabetes Prediction Web Application:**

    * Make sure you have all the dependencies installed, you can install them using pip:
        ```bash
        pip install pandas numpy scikit-learn streamlit
        ```
    * Place the `diabetes_webpage.py`, the trained model file (`trained_model.sav`), and the scaler file (`scaler.sav`) in the same directory.
    * Run the script from the command line using Streamlit:
        ```bash
        streamlit run diabetes_webpage.py
        ```
    * The web application will open in your default web browser.
    * Enter the required health information and click the "Diabetes Test Result" button to get the prediction.

##   Important Notes

* The model's performance is dependent on the quality and representativeness of the training data.
* This system is intended for informational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for diagnosis and treatment.
* The `diabetes_webpage.py` script includes error handling for invalid user inputs, ensuring the application's robustness.
```