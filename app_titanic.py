# app_titanic.py

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load Titanic model
with open('titanic_classification.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Titanic Survival Prediction App 🚢")
st.write("Will you survive the Titanic disaster? Let's find out!")

# User Inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", options=[1, 2, 3])
sex = st.selectbox("Sex", options=["male", "female"])
age = st.number_input("Age", min_value=0.42, max_value=80.0, value=30.0)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=8, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=6, value=0)
fare = st.number_input("Fare Paid", min_value=0.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", options=["C", "Q", "S"])

# Mapping categorical data
sex_mapped = 1 if sex == "female" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked_mapped = embarked_map[embarked]

# Predict button
if st.button("Predict Survival"):
    input_data = np.array([[pclass, sex_mapped, age, sibsp, parch, fare, embarked_mapped]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🟢 Survived!")
    else:
        st.error("🔴 Did not survive.")
