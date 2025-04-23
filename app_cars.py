# app_cars.py

import streamlit as st
import pandas as pd
import joblib

# Load the regression model pipeline
model = joblib.load("car_price_regressor_v2.pkl")

# Load model options from CSV
df = pd.read_csv("cars.csv")

# Streamlit UI
st.title("🚗 Car Price Prediction App")
st.write("Predict the estimated price of a car based on its features.")

# Input fields
brand = st.selectbox("Brand", sorted(df['Brand'].dropna().unique()))

# Filter model list based on selected brand
filtered_models = df[df['Brand'] == brand]['Model'].dropna().unique()
model_name = st.selectbox("Model", sorted(filtered_models))

year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020)
mileage = st.number_input("Mileage (in km)", min_value=0.0, max_value=500000.0, value=50000.0)
engine_power = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, value=2.0)
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic", "Semi-Automatic"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric", "Hybrid"])
doors = st.number_input("Number of Doors", min_value=1, max_value=5, value=4)
owner_count = st.number_input("Number of Previous Owners", min_value=1, max_value=5, value=1)

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        'Brand': brand,
        'Model': model_name,
        'Year': year,
        'Mileage': mileage,
        'Engine_Size': engine_power,
        'Transmission': transmission,
        'Fuel_Type': fuel_type,
        'Doors': doors,
        'Owner_Count': owner_count
    }])

    # Predict the numeric price
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Predicted Car Price: **${predicted_price:,.2f}**")
