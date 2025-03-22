
import pandas as pd
import numpy as np
from google.colab import files

# Upload dataset
uploaded = files.upload()

# Load the dataset
diabetes_dataset = pd.read_csv("diabetes.csv")

# Display first few rows
diabetes_dataset.head()

# Checking class distribution
print(diabetes_dataset['Outcome'].value_counts())

# Splitting data into features (X) and labels (Y)
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

# Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Standardizing the data (only fit on training data)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn import svm
from sklearn.metrics import accuracy_score

# Train the SVM model
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Accuracy on training data
X_train_pred = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_pred, Y_train)
print(f"Training Accuracy: {training_data_accuracy:.4f}")

# Accuracy on testing data
X_test_pred = classifier.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_pred, Y_test)
print(f"Testing Accuracy: {testing_data_accuracy:.4f}")

import pickle

# Save the trained model
filename = 'trained_model.sav'
pickle.dump(classifier, open(filename, 'wb'))

# Load the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))
print("Model Loaded Successfully!")

# Example input data
input_data = (4, 110, 92, 0, 0, 37.6, 0.191, 30)

# Convert input data to numpy array and reshape
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

# Standardize input data using the same scaler
std_data = scaler.transform(input_data_as_numpy_array)

# Make a prediction
prediction = loaded_model.predict(std_data)

# Output the result
if prediction[0] == 0:
    print("The person is NOT diabetic")
else:
    print("The person IS diabetic")

# Save the fitted scaler
pickle.dump(scaler, open("scaler.sav", "wb"))
