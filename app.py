import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('placement_model.pkl')

# Streamlit UI
st.title('Student Placement Prediction')

st.header('Enter Student Details')
cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input('IQ', min_value=0, max_value=300, step=1)

if st.button('Predict Placement'):
    example = np.array([[cgpa, iq]])
    prediction = model.predict(example)
    result = 'Placed' if prediction[0] == 1 else 'Not Placed'
    st.write(f'The student is: **{result}**')
