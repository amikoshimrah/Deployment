# app_cars.py

import streamlit as st
import numpy as np
import joblib

# Load the compressed model
model = joblib.load("car_price_classifier_compressed.pkl")


# Streamlit UI
st.title("🚗 Car Price Prediction App")
st.write("Predict the price category of a car based on its features.")

# Define encoding maps (must match what the model was trained with)
brand_map = {"Toyota": 0, "BMW": 1, "Ford": 2, "Hyundai": 3, "Mercedes": 4, "Honda": 5}
transmission_map = {"Manual": 0, "Automatic": 1, "Semi-Automatic": 2}
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2, "Electric": 3}

# User input fields
brand = st.selectbox("Brand", options=list(brand_map.keys()))
year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020)
mileage = st.number_input("Mileage (km/l)", min_value=1.0, max_value=40.0, value=15.0)
engine_power = st.number_input("Horsepower", min_value=30, max_value=800, value=120)
transmission = st.selectbox("Transmission Type", options=list(transmission_map.keys()))
fuel_type = st.selectbox("Fuel Type", options=list(fuel_map.keys()))

# Label map for prediction
predicted_price = model.predict(input_data)[0]
st.success(f"💰 Predicted Car Price: **${predicted_price:,.2f}**")

# Predict button
if st.button("Predict Price Category"):
    # Encode categorical features
    input_data = np.array([[
        brand_map[brand],
        year,
        mileage,
        engine_power,
        transmission_map[transmission],
        fuel_map[fuel_type]
    ]])

    prediction = model.predict(input_data)[0]
    predicted_label = label_map.get(prediction, "Unknown")

    st.success(f"💰 Predicted Price Category: **{predicted_label}**")
