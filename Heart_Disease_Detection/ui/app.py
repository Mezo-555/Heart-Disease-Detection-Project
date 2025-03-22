import streamlit as st
import sys

# Ensure the correct project directory is in the system path
BASE_DIR = r"C:\Users\moata\Documents\Projects\Intelligent Systems\Heart_Disease_Detection"
sys.path.append(BASE_DIR)

from ml_model.predict import predict_heart_disease
from rule_based_system.expert_system import assess_risk

st.title("Heart Disease Risk Prediction")
st.sidebar.header("Enter Patient Information")

# User input fields
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.sidebar.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
chol = st.sidebar.number_input("Cholesterol Level", min_value=100, max_value=400, value=200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.sidebar.selectbox("Resting ECG", [0, 1, 2])
thalach = st.sidebar.number_input("Maximum Heart Rate", min_value=60, max_value=220, value=150)
exang = st.sidebar.selectbox("Exercise-Induced Angina", [0, 1])
oldpeak = st.sidebar.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, value=1.0)
slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.sidebar.selectbox("Number of Major Vessels Colored", [0, 1, 2, 3])
thal = st.sidebar.selectbox("Thalassemia Type", [1, 2, 3])

input_data = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

if st.sidebar.button("Predict"):
    model_prediction = predict_heart_disease(input_data)
    expert_prediction = assess_risk(input_data)  # Now using expert_system.py
    
    st.subheader("Results")
    st.write(f"**Decision Tree Model Prediction:** {model_prediction}")
    st.write(f"**Expert System Prediction:** {expert_prediction}")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using Streamlit")

# streamlit run ui/app.py