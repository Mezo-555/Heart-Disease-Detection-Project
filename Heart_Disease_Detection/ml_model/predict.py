import pandas as pd
import joblib

# Load Trained Model
model = joblib.load("ml_model/decision_tree_model.pkl")

# Function to Make Predictions
def predict_heart_disease(input_data):
    df = pd.DataFrame([input_data])
    
    # Ensure all required features are present
    expected_features = model.feature_names_in_
    for feature in expected_features:
        if feature not in df.columns:
            df[feature] = 0  # Fill missing features with 0
    df = df[expected_features]  # Align column order
    
    prediction = model.predict(df)
    risk = "High Risk" if prediction[0] == 1 else "Low Risk"
    return risk

if __name__ == "__main__":
    # Example input data (modify as needed)
    example_data = {
        "age": 0.47916666666666663,
        "sex": 1,
        "trestbps": 0.2924528301886792,
        "chol": 0.1963470319634703,
        "thalach": 0.7404580152671755,
        "exang": 0,
        "oldpeak": 0.16129032258064516,
        "cp_0": 0.0,
        "cp_1": 1.0,
        "cp_2": 0.0,
        "restecg_0.0": 0.0,
        "restecg_1.0": 1.0,
        "slope_1": 0.0,
        "slope_2": 1.0,
        "ca_0": 0.0,
        "ca_1": 0.0,
        "ca_2": 1.0,
        "ca_3": 0.0,
        "thal_1": 0.0,
        "thal_2": 0.0,
        "thal_3": 1.0
    }
    
    result = predict_heart_disease(example_data)
    print(f"Prediction: {result}")
