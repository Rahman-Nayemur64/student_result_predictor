import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("best_model.pkl")

st.title("Student exam score predictor")

study_hour = st.slider("Study Hours per day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance percentage",0.0,100.0, 80.0 )
mental_health = st.slider("Mental Health Rating (1 to 10)",1,10,5)
sleep_hous = st.slider("Sleep Hours per day", 0.0, 12.0, 7.0)
part_time_job = st.selectbox("Do you have a part-time job?", ["Yes", "No"])

ptj_encoded = 1 if part_time_job == "Yes" else 0

if st.button("Predict Exam Score"):
    input_data = np.array([[study_hour, attendance, mental_health, sleep_hous, ptj_encoded]])
    prediction = model.predict(input_data)
    
    prediction = max(0, min(100, prediction)) 
    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")