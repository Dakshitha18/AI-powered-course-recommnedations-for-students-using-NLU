import streamlit as st
import pandas as pd
import joblib

# Load the best model from the saved file
best_model = joblib.load(r"C:\Users\reddy\OneDrive\Desktop\student councelor\student councelor\best_course_title_prediction_model.joblib")

# Streamlit App

st.title('Course Title Prediction App')

# User Input Section
st.header('Enter Course Details:')
price = st.number_input('Enter the course price:', min_value=0.0)
num_reviews = st.number_input('Enter the number of reviews:', min_value=0)
num_lectures = st.number_input('Enter the number of lectures:', min_value=0)
content_duration = st.number_input('Enter the content duration in hours:', min_value=0.0)

# Predictions
if st.button('Predict Course Title'):
    # Create a DataFrame with the user inputs
    user_inputs = pd.DataFrame({
        'price': [price],
        'num_reviews': [num_reviews],
        'num_lectures': [num_lectures],
        'content_duration': [content_duration]
    })

    # Make predictions using the loaded model
    predicted_course_title = best_model.predict(user_inputs)

    # Display the predicted course title
    st.success(f'Predicted Course Title: {predicted_course_title[0]}')