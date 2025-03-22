import pandas as pd
import sys
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Ensure correct module import path
BASE_DIR = r"C:\Users\moata\Documents\Projects\Intelligent Systems\Heart_Disease_Detection"
sys.path.append(BASE_DIR)

from rule_based_system.rules import HeartDiseaseRisk, HeartDiseaseExpert
# Load Test Data
df = pd.read_csv("data/cleaned_data.csv")

# Extract Features & Labels
X_test = df.drop(columns=["target"])
y_test = df["target"]

# Initialize Expert System
engine = HeartDiseaseExpert()
engine.reset()

def make_predictions():
    # Make Predictions
    predictions = []
    for _, row in X_test.iterrows():
        engine.reset()  # Reset engine for each case
        engine.declare(HeartDiseaseRisk(**row.to_dict()))
        engine.run()

        # Determine risk output (assuming final risk is stored in engine.risk_levels)
        predicted_risk = 1 if "high" in engine.risk_levels else 0
        predictions.append(predicted_risk)

    # Calculate Metrics
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

def assess_risk(input_data):
    engine = HeartDiseaseExpert()
    engine.reset()
    engine.declare(HeartDiseaseRisk(**input_data))
    engine.run()
    engine.declare_final_risk()
    engine.run()
    if not engine.risk_levels:
        return "Unknown Risk"  # Default if no rules fire
    
    return max(engine.risk_levels, key=lambda x: ['low', 'moderate', 'high', 'very high'].index(x))

# User Input Function
def assess_risk_manual():
    engine = HeartDiseaseExpert()
    engine.reset()
    
    print("Enter patient details:")
    age = int(input("Age: "))
    sex = int(input("Sex (0 = Female, 1 = Male): "))
    cp = int(input("Chest Pain Type (0-3): "))
    trestbps = int(input("Resting Blood Pressure: "))
    chol = int(input("Cholesterol Level: "))
    fbs = int(input("Fasting Blood Sugar > 120? (0 = No, 1 = Yes): "))
    restecg = int(input("Resting ECG (0-2): "))
    thalach = int(input("Maximum Heart Rate: "))
    exang = int(input("Exercise Induced Angina (0 = No, 1 = Yes): "))
    oldpeak = float(input("ST Depression Induced by Exercise: "))
    slope = int(input("Slope of Peak Exercise ST Segment (0-2): "))
    ca = int(input("Number of Major Vessels Colored (0-3): "))
    thal = int(input("Thalassemia Type (1-3): "))
    
    engine.declare(HeartDiseaseRisk(age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol,
                                    fbs=fbs, restecg=restecg, thalach=thalach, exang=exang,
                                    oldpeak=oldpeak, slope=slope, ca=ca, thal=thal))
    engine.run()
    engine.declare_final_risk()
    engine.run()