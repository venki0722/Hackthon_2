import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("renewable_model_1.pkl")

st.title("🔆 Tamil Nadu Renewable Energy Forecast")

humidity = st.number_input("Humidity (%)")
pressure = st.number_input("Pressure (mb)")
wind_speed = st.number_input("Wind Speed (km/h)")

if st.button("Predict Energy"):

    input_data = np.array([[humidity, pressure, wind_speed]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Energy Output: {prediction}")
