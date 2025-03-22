import pandas as pd
import joblib
import os
from sklearn.preprocessing import MinMaxScaler

# Define paths
BASE_DIR = r"C:\Users\moata\Documents\Projects\Intelligent Systems\Heart_Disease_Detection"
model_path = os.path.join(BASE_DIR, "ml_model", "decision_tree_model.pkl")
scaler_path = os.path.join(BASE_DIR, "utils", "scaler.pkl")

# Load trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path) if os.path.exists(scaler_path) else MinMaxScaler()

# Feature names used during training
categorical_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]
numerical_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]

def preprocess_input(input_data):
    df = pd.DataFrame([input_data])
    
    # One-Hot Encoding
    df = pd.get_dummies(df, columns=categorical_cols)
    
    # Ensure all expected features are present
    expected_features = model.feature_names_in_
    for feature in expected_features:
        if feature not in df.columns:
            df[feature] = 0  # Fill missing categories with 0
    df = df[expected_features]  # Align column order
    
    # Normalize numerical features
    df[numerical_cols] = scaler.transform(df[numerical_cols])
    
    return df

def predict_heart_disease(input_data):
    df = preprocess_input(input_data)
    prediction = model.predict(df)
    risk = "High Risk" if prediction[0] == 1 else "Low Risk"
    return risk

if __name__ == "__main__":
    # Example input data (modify as needed)
    example_data = {
        "age": 50,
        "sex": 1,
        "cp": 0,
        "trestbps": 130,
        "chol": 200,
        "fbs": 1,
        "restecg": 1,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 1.0,
        "slope": 1,
        "ca": 1,
        "thal": 2
    }
    
    result = predict_heart_disease(example_data)
    print(f"Prediction: {result}")
