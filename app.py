import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Streamlit app title
st.title('Water Potability Prediction')

# Description
st.write("This app predicts whether water is potable or not based on several features.")

# Input fields for the user to enter the features
ph = st.number_input('PH Level', min_value=0.0, max_value=14.0, value=7.0)
sulfate = st.number_input('Sulfate', min_value=0.0, max_value=500.0, value=200.0)
trihalomethanes = st.number_input('Trihalomethanes', min_value=0.0, max_value=500.0, value=100.0)
turbidity = st.number_input('Turbidity', min_value=0.0, max_value=100.0, value=30.0)
chloramines = st.number_input('Chloramines', min_value=0.0, max_value=100.0, value=50.0)
conductivity = st.number_input('Conductivity', min_value=0.0, max_value=1000.0, value=300.0)

# Create a list with the features entered by the user
user_input = np.array([ph, sulfate, trihalomethanes, turbidity, chloramines, conductivity]).reshape(1, -1)

# Prediction button
if st.button('Predict'):
    # Make a prediction
    prediction = model.predict(user_input)
    result = "Potable" if prediction[0] == 1 else "Not Potable"
    st.write(f"The water is: {result}")
