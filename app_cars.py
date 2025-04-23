# app_cars.py

import streamlit as st
import numpy as np
import joblib  # use joblib instead of pickle

# Load the compressed model
model = joblib.load("car_price_classifier_compressed.pkl")

# Streamlit UI
st.title("🚗 Car Price Prediction App")
st.write("Predict the price category of a car based on its features.")

# User input fields
brand = st.selectbox("Brand", options=["Toyota", "BMW", "Ford", "Hyundai", "Mercedes", "Honda"])
year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020)
mileage = st.number_input("Mileage (km/l)", min_value=1.0, max_value=40.0, value=15.0)
engine_power = st.number_input("Horsepower", min_value=30, max_value=800, value=120)
transmission = st.selectbox("Transmission Type", options=["Manual", "Automatic", "Semi-Automatic"])
fuel_type = st.selectbox("Fuel Type", options=["Petrol", "Diesel", "CNG", "Electric"])

# Label map for prediction
label_map = {0: "Low Price", 1: "Medium Price", 2: "High Price"}

# Predict button
if st.button("Predict Price Category"):
    input_data = np.array([[brand, year, mileage, engine_power, transmission, fuel_type]])
    prediction = model.predict(input_data)[0]
    predicted_label = label_map.get(prediction, "Unknown")

    st.success(f"💰 Predicted Price Category: **{predicted_label}**")
