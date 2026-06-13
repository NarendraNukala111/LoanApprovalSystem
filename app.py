import streamlit as st
import joblib
import numpy as np

# load trained model
model = joblib.load("model.pkl")

st.title("Student Performance Predictor")

# user inputs
hours = st.number_input("Study Hours")
sleep = st.number_input("Sleep Hours")

if st.button("Predict"):
    prediction = model.predict([[hours, sleep]])
    st.success(f"Prediction: {prediction[0]}")