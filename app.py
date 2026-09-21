import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Iris Flower Prediction")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

input_data = np.array([[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction[0])
