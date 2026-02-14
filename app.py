import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("renewable_model.pkl")

st.title("🔆 Tamil Nadu Renewable Energy Forecast")

# Define EXACT feature names used in training
feature_names = ["Humidity_Pct", "Pressure_mb", "WindSpeed_kmh"]

input_data = []

for feature in feature_names:
    value = st.number_input(f"Enter {feature}")
    input_data.append(value)

if st.button("Predict Energy"):
    input_array = np.array([input_data])
    prediction = model.predict(input_array)

    st.success(f"Prediction (Solar, Wind, Total MW): {prediction}")
