import joblib
import numpy as np
import streamlit as st

# Load model + scaler
model = joblib.load("heart_rf_model.pkl")
scaler = joblib.load("heart_scaler.pkl")

st.title("🫀 Heart Disease Predictor")

# User input
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0–3)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
restecg = st.selectbox("Resting ECG (0–2)", [0,1,2])
thalach = st.number_input("Max Heart Rate", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope (0–2)", [0,1,2])
ca = st.selectbox("Major Vessels (0–3)", [0,1,2,3])
thal = st.selectbox("Thalassemia (1,2,3)", [1,2,3])

# Convert sex to numeric
sex = 1 if sex == "Male" else 0

# Prediction
if st.button("Predict"):
    user_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                           thalach, exang, oldpeak, slope, ca, thal]])
    
    # Scale input
    user_data_scaled = scaler.transform(user_data)
    
    prediction = model.predict(user_data_scaled)
    
    if prediction[0] == 0:
        st.success("✅ No Heart Disease Detected")
    else:
        st.error("⚠️ High Risk of Heart Disease")
