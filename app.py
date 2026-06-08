import streamlit as st
import pickle

# Load model
model = pickle.load(open('iris_model.pkl', 'rb'))

# Title
st.title("Iris Flower Classification")

st.write("Enter flower measurements")

# Inputs
sepal_length = st.number_input("Sepal Length")

sepal_width = st.number_input("Sepal Width")

petal_length = st.number_input("Petal Length")

petal_width = st.number_input("Petal Width")

# Prediction
if st.button("Predict"):

    prediction = model.predict([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    species = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    st.success(
        f"Predicted Flower: {species[prediction[0]]}"
    )