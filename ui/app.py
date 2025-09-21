# ===== app.py =====
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved model
model = joblib.load(r"D:\pdfs\Heart_Disease_Project\models\final_model.pkl")

st.title(" Heart Disease Prediction App")
st.write("Enter the patient's data to predict the risk of heart disease.")

# User input fields
thalach = st.number_input("Maximum heart rate (thalach)", min_value=50, max_value=210, value=150)
thal = st.selectbox("Thal (3 = normal, 6 = fixed defect, 7 = reversible defect)", [3, 6, 7])
cp = st.selectbox("Chest pain type (cp: 0–3)", [0, 1, 2, 3])
ca = st.number_input("Number of major vessels (ca: 0–3)", min_value=0, max_value=3, value=0)
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=6.0, step=0.1, value=1.0)

# Prediction button
if st.button(" Predict"):
    input_data = pd.DataFrame({
        "thalach": [thalach],
        "thal": [thal],
        "cp": [cp],
        "ca": [ca],
        "oldpeak": [oldpeak]
    })

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f" Result: The patient is at risk of heart disease with a probability of {prob:.2%}")
    else:
        st.success(f" Result: The patient is not at risk of heart disease with a probability of {(1 - prob):.2%}")