## 📰 Fake News Detection App

A Machine Learning and NLP-based web app to classify news as **Real** or **Fake** using four different classifiers. Built with **Scikit-learn**, **Streamlit**, and trained on a labeled dataset of news articles.

---

### 🚀 Features

* Enter any news content and detect if it's **Fake** or **Real**
* Runs predictions using 4 ML models:

  * Logistic Regression
  * Decision Tree
  * Gradient Boosting
  * Random Forest
* Simple, clean Streamlit interface
* Reproducible and easy to deploy locally or on the cloud

---

### 🧠 How It Works

1. The input news content is **preprocessed** using regex and string cleaning.
2. It is then **vectorized** using a trained TF-IDF vectorizer.
3. Each classifier makes a prediction.
4. Predictions are displayed instantly in the UI.

---

### 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-learn
* **Data Preprocessing:** NLTK, regex, pandas
* **Model Serialization:** Joblib

---

### 📦 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/fake-news-detection-app.git
   cd fake-news-detection-app
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Unix/macOS
   venv\Scripts\activate     # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run streamlit_app.py
   ```

---

### 🧪 Example Input

```
Breaking: Scientists discover new technique to prevent cyberattacks on global health infrastructure...
```

### ✅ Example Output

```
Logistic Regression: Real News  
Decision Tree: Fake News  
Gradient Boosting: Real News  
Random Forest: Real News
```

---

### 🧾 Files Included

* `streamlit_app.py`: Streamlit interface code
* `lr_model.pkl`, `dt_model.pkl`, `gb_model.pkl`, `rf_model.pkl`: Trained classifiers
* `vectorizer.pkl`: TF-IDF vectorizer used for text transformation
* `Fake_News_Detection.ipynb`: Notebook used to build and train the models

### 🤝 Contributions
**Contributions, suggestions, and improvements are welcome!**
If you find a bug or have an idea to enhance the project, feel free to open an issue or submit a pull request. Let's make this better together!


