from rules import HeartDiseaseRisk, HeartDiseaseExpert

# User Input Function
def assess_risk():
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

if __name__ == "__main__":
    assess_risk()
