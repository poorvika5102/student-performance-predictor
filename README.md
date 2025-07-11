# 🎓 Student Performance Predictor

This is a machine learning project that predicts whether a student is likely to **pass or fail** based on their academic habits and lifestyle factors.

🚀 Built with **Python, scikit-learn, and Streamlit**, this project demonstrates my ability to work with real-world data, build ML models, and deploy them through interactive web apps — showcasing my AI/ML skills.

---

## 💡 Features

- Random Forest model with 85%+ accuracy
- Real-time predictions via Streamlit app
- Input features: study time, failures, absences, health, and free time
- Clean ML pipeline: preprocessing → training → evaluation → deployment

---

## 📁 Project Structure

```
student-performance-predictor/
├── app.py                 → Streamlit web app
├── model.ipynb            → Jupyter notebook for training
├── model.pkl              → Saved trained model
├── student_data.csv       → Dataset used
├── requirements.txt       → List of dependencies
└── README.md              → Project documentation
```

---

## 📊 Dataset

- Source: [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
- CSV version used: [`student-data.csv`](https://github.com/mohammedAljadd/students-performance-prediction/blob/main/student-data.csv)
- Target variable: `passed` → converted to 0 (fail) or 1 (pass)

---

## 🧠 Model Info

- 📌 Algorithm: `RandomForestClassifier`
- 🧰 Libraries: `scikit-learn`, `pandas`, `numpy`, `joblib`, `streamlit`
- 🧪 Metrics: Accuracy score and confusion matrix

---

## ▶️ Run Locally

```bash
# Clone the repo
git clone https://github.com/poorvika5102/student-performance-predictor
cd student-performance-predictor

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🙋‍♀️ About Me

**Poorvika A C**  
Aspiring AI/ML Developer | Passionate about building real-world solutions using AI  

---

> ⭐ If you like this project, feel free to star the repo and connect with me!
