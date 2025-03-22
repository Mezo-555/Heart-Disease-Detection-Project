from experta import *

class HeartDiseaseRisk(Fact):
    """Fact container for heart disease risk assessment"""
    pass

class HeartDiseaseExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.risk_levels = set()

    # Start with single conditions
    @Rule(HeartDiseaseRisk(chol=P(lambda x: x > 240)))
    def high_risk_high_cholesterol(self):
        self.risk_levels.add('high')
        print("High Risk: High Cholesterol")
    
    @Rule(HeartDiseaseRisk(age=P(lambda x: x > 50)))
    def moderate_risk_age(self):
        self.risk_levels.add('moderate')
        print("Moderate Risk: Age over 50")
    
    @Rule(HeartDiseaseRisk(trestbps=P(lambda x: x > 140)))
    def high_risk_bp(self):
        self.risk_levels.add('high')
        print("High Risk: High Blood Pressure")
    
    @Rule(HeartDiseaseRisk(thalach=P(lambda x: x < 100)))
    def high_risk_low_thalach(self):
        self.risk_levels.add('high')
        print("High Risk: Low Maximum Heart Rate")
    
    # Increase complexity with AND conditions
    @Rule(HeartDiseaseRisk(chol=P(lambda x: x > 240), age=P(lambda x: x > 50)))
    def high_risk_cholesterol_age(self):
        self.risk_levels.add('high')
        print("High Risk: High Cholesterol and Age over 50")
    
    @Rule(HeartDiseaseRisk(trestbps=P(lambda x: x > 140), exang=1))
    def high_risk_bp_exang(self):
        self.risk_levels.add('high')
        print("High Risk: High Blood Pressure and Exercise-Induced Angina")
    
    @Rule(HeartDiseaseRisk(thalach=P(lambda x: x < 100), oldpeak=P(lambda x: x > 2.0)))
    def high_risk_low_thalach_oldpeak(self):
        self.risk_levels.add('high')
        print("High Risk: Low Maximum Heart Rate and High ST Depression")
    
    @Rule(HeartDiseaseRisk(sex=1, age=P(lambda x: x > 60)))
    def high_risk_male_senior(self):
        self.risk_levels.add('high')
        print("High Risk: Senior Male Patient")
    
    @Rule(HeartDiseaseRisk(cp=2, restecg=1))
    def moderate_risk_cp_restecg(self):
        self.risk_levels.add('moderate')
        print("Moderate Risk: Chest Pain Type 2 and Rest ECG Type 1")
    
    @Rule(HeartDiseaseRisk(cp=0, slope=1, ca=0))
    def low_risk_no_angina(self):
        self.risk_levels.add('low')
        print("Low Risk: No Chest Pain, Normal Slope, No Major Vessels Colored")
    
    @Rule(HeartDiseaseRisk(thal=3, oldpeak=P(lambda x: x > 2.5)))
    def high_risk_thal_oldpeak(self):
        self.risk_levels.add('high')
        print("High Risk: Thalassemia Type 3 and High ST Depression")
    
    @Rule(HeartDiseaseRisk(fbs=1, trestbps=P(lambda x: x > 130)))
    def high_risk_fbs_bp(self):
        self.risk_levels.add('high')
        print("High Risk: Fasting Blood Sugar > 120 and High Blood Pressure")
    
    @Rule(HeartDiseaseRisk(family_history=True, age=P(lambda x: x > 45)))
    def moderate_risk_family_history(self):
        self.risk_levels.add('moderate')
        print("Moderate Risk: Family History and Age over 45")
    
    @Rule(HeartDiseaseRisk(age=P(lambda x: x < 40), chol=P(lambda x: x < 200), thalach=P(lambda x: x > 150)))
    def low_risk_young_high_thalach(self):
        self.risk_levels.add('low')
        print("Low Risk: Young Age, Healthy Cholesterol, and High Maximum Heart Rate")
    
    @Rule(HeartDiseaseRisk(trestbps=P(lambda x: x > 160), age=P(lambda x: x > 65)))
    def high_risk_hypertension_elderly(self):
        self.risk_levels.add('high')
        print("High Risk: Severe Hypertension in Elderly")
    
    @Rule(HeartDiseaseRisk(cp=3, thal=3, oldpeak=P(lambda x: x > 3.0)))
    def very_high_risk_angina_thal(self):
        self.risk_levels.add('very high')
        print("Very High Risk: Severe Chest Pain, Thalassemia Type 3, and High ST Depression")
    
    @Rule(AS.f1 << Fact(risk=MATCH.r))
    def show_risk(self, f1, r):
        print(f"Final Risk Assessment: {r.capitalize()}\n")

    def declare_final_risk(self):
        if self.risk_levels:
            risk_priority = ['low', 'moderate', 'high', 'very high']
            final_risk = max(self.risk_levels, key=risk_priority.index)
            self.declare(Fact(risk=final_risk))

# Example Usage
if __name__ == "__main__":
    engine = HeartDiseaseExpert()
    engine.reset()
    engine.declare(HeartDiseaseRisk(age=55, sex=1, trestbps=145, chol=250, thalach=95, exang=1, oldpeak=2.8, cp=2, restecg=1, slope=1, ca=0, thal=3, fbs=1))  # Example input
    engine.run()
    engine.declare_final_risk()
    engine.run()