import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('nextgentipper_model.pkl')

# App title
st.title("Generous Tipper Predictor")

# User inputs
passenger_count = st.slider("Passenger Count", 1, 6, 1)
avg_distance = st.slider("Average Trip Distance (miles)", 0.5, 30.0, 2.0, step=0.5)
month = st.selectbox("Month", ['jan', 'feb', 'mar', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
weekday = st.selectbox("Day of Week", ['monday', 'tuesday', 'wednesday', 'thursday', 'saturday', 'sunday'])
time_zone = st.selectbox("Time of Day", ['am_rush', 'daytime', 'pm_rush', 'nighttime'])

# Feature columns expected by model
feature_cols = [
    'passenger_count', 'avg_distance',
    'am_rush', 'daytime', 'pm_rush', 'nighttime',
    'day_monday', 'day_saturday', 'day_sunday', 'day_thursday', 'day_tuesday', 'day_wednesday',
    'month_aug', 'month_dec', 'month_feb', 'month_jan', 'month_jul', 'month_jun',
    'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep'
]

# Initialize feature values
input_data = dict.fromkeys(feature_cols, 0)

# Set fixed inputs
input_data['passenger_count'] = passenger_count
input_data['avg_distance'] = avg_distance
input_data[time_zone] = 1
input_data[f'day_{weekday}'] = 1
input_data[f'month_{month}'] = 1

# Create DataFrame for prediction
input_df = pd.DataFrame([input_data])

# Predict and show result
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("✅ This customer is likely a generous tipper!")
    else:
        st.warning("⚠️ This customer is likely *not* a generous tipper.")
