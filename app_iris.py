# app_iris.py

import streamlit as st
import numpy as np
import pickle

# Load the model
with open("iris_classifier_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("🌸 Iris Species Prediction App")
st.write("Predict the Iris flower species based on measurements.")

# Input fields for features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, value=0.2)

# Label map
label_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

# Predict button
if st.button("Predict Species"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    predicted_label = label_map.get(prediction, "Unknown")

    st.success(f"🌼 Predicted Iris Species: **{predicted_label}**")
