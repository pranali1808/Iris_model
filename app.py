import streamlit as st
import numpy as np
import pickle

# Your inputs
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

prediction = model.predict(input_data)
