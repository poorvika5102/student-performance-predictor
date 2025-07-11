import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("🎓 Student Performance Predictor")
st.markdown("Enter the student's details below to predict if they'll pass or fail.")

# Input form
studytime = st.slider("🕓 Study Time (1-4)", min_value=1, max_value=4, step=1)
failures = st.slider("❌ Number of Past Failures", min_value=0, max_value=3, step=1)
absences = st.slider("🏫 Absences", min_value=0, max_value=100, step=1)
health = st.slider("💖 Health (1 = worst, 5 = best)", min_value=1, max_value=5, step=1)
freetime = st.slider("🕒 Free Time (1-5)", min_value=1, max_value=5, step=1)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[studytime, failures, absences, health, freetime]],
                              columns=['studytime', 'failures', 'absences', 'health', 'freetime'])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The student is likely to **PASS**! 🎉")
    else:
        st.error("❌ The student is likely to **FAIL**. 🛑")
