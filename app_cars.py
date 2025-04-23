# app_cars.py

import streamlit as st
import pandas as pd
import joblib

# Load the regression model pipeline
model = joblib.load("car_price_regressor.pkl")

# Streamlit UI
st.title("🚗 Car Price Prediction App")
st.write("Predict the estimated price of a car based on its features.")

# Input fields
brand = st.selectbox("Brand", ["Toyota", "BMW", "Ford", "Hyundai", "Mercedes", "Honda", "Audi", "Volkswagen", "Chevrolet", "Kia", "Mercedes"])
year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020)
mileage = st.number_input("Mileage (in km)", min_value=0.0, max_value=500000.0, value=50000.0)
engine_power = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, value=2.0)
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic", "Semi-Automatic"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric", "Hybrid"])

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        'Brand': brand,
        'Year': year,
        'Mileage': mileage,
        'Engine_Size': engine_power,
        'Transmission': transmission,
        'Fuel_Type': fuel_type
    }])

    # Predict the numeric price
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Predicted Car Price: **${predicted_price:,.2f}**")
