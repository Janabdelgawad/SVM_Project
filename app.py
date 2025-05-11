import streamlit as st
import pandas as pd
import numpy as np
import joblib

pipeline = joblib.load("diabetes_pipeline.joblib")
input_data = np.array([list(features.values())]).astype(float)
prediction = pipeline.predict(input_data)


st.title("🩺 Diabetes Risk Classifier")
st.markdown("This app predicts whether an individual is at risk of diabetes based on health indicators.")

# Input fields for all 21 features
features = {
    "GenHlth": st.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 3),
    "BMI": st.number_input("BMI", 10.0, 60.0, 25.0),
    "HighBP": st.selectbox("High Blood Pressure", [0, 1]),
    "Age": st.slider("Age", 18, 100, 40),
    "HighChol": st.selectbox("High Cholesterol", [0, 1]),
    "CholCheck": st.selectbox("Cholesterol Check in Last 5 Years", [0, 1]),
    "HvyAlcoholConsump": st.selectbox("Heavy Alcohol Consumption", [0, 1]),
    "Income": st.slider("Income Level (1=Low, 8=High)", 1, 8, 4),
    "Sex": st.selectbox("Sex (0=Female, 1=Male)", [0, 1]),
    "HeartDiseaseorAttack": st.selectbox("Heart Disease or Attack", [0, 1]),
    "PhysHlth": st.slider("Physical Health (days unwell in past 30)", 0, 30, 5),
    "DiffWalk": st.selectbox("Difficulty Walking", [0, 1]),
    "Stroke": st.selectbox("Ever had a Stroke", [0, 1]),
    "MentHlth": st.slider("Mental Health (days unwell in past 30)", 0, 30, 5),
    "Education": st.slider("Education Level (1=Low, 6=High)", 1, 6, 4),
    "PhysActivity": st.selectbox("Physical Activity", [0, 1]),
    "Veggies": st.selectbox("Eats Vegetables Regularly", [0, 1]),
    "AnyHealthcare": st.selectbox("Has Any Healthcare Coverage", [0, 1]),
    "Fruits": st.selectbox("Eats Fruits Regularly", [0, 1]),
    "Smoker": st.selectbox("Smoker", [0, 1]),
    "NoDocbcCost": st.selectbox("Couldn’t See Doctor Due to Cost", [0, 1]),
}

# Convert input to array
input_data = np.array([list(features.values())]).astype(float)

# Predict when button is clicked
if st.button("Predict"):
    input_lda = lda.transform(input_data)           # Step 1: LDA transformation
    input_scaled = scaler.transform(input_lda)      # Step 2: Apply scaling
    prediction = model.predict(input_scaled)        # Step 3: SVM prediction

    if prediction[0] == -1:
        st.error("⚠️ The model predicts: **Diabetes or Prediabetes**")
    else:
        st.success("✅ The model predicts: **No Diabetes**")
