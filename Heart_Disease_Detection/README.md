# Heart Disease Detection Project

## 📌 Project Overview
This project aims to detect heart disease using **two approaches**:
1. **Rule-Based Expert System** (built with `Experta`)
2. **Machine Learning Model** (Decision Tree using `Scikit-Learn`)

The goal is to **compare the accuracy and explainability** of both methods.

---

## 📂 Folder Structure
```
Heart_Disease_Detection/
│── data/ # Contains the dataset (raw & cleaned)
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│── notebooks/ # Jupyter Notebooks for visualization & preprocessing
│   ├── data_analysis.ipynb
│   ├── model_training.ipynb
│── rule_based_system/ # Rule-based system using Experta
│   ├── rules.py
│   ├── expert_system.py
│── ml_model/ # Decision Tree implementation
│   ├── train_model.py
│   ├── predict.py
│── utils/ # Helper functions for data cleaning & processing
│   ├── data_processing.py
│── reports/ # Comparison reports and evaluation
│   ├── accuracy_comparison.md
│── ui/ # Streamlit UI for user interaction
│   ├── app.py
│── README.md # Project documentation & setup instructions
│── requirements.txt # List of dependencies
```

---

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/Heart_Disease_Detection.git
cd Heart_Disease_Detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Data Processing
```bash
python utils/data_processing.py
```

### 4️⃣ Train the Decision Tree Model
```bash
python ml_model/train_model.py
```

### 5️⃣ Run Predictions
```bash
python ml_model/predict.py
```

### 6️⃣ Run Expert System
```bash
python rule_based_system/expert_system.py
```

---

## 🏆 Comparison: Decision Tree vs. Expert System
The **Decision Tree Model** is trained using **GridSearchCV** for hyperparameter tuning, while the **Expert System** relies on predefined medical rules.

🔹 **Decision Tree** → Higher accuracy, but less explainable.  
🔹 **Expert System** → More interpretable, but may generalize poorly.  

For detailed results, see **`reports/accuracy_comparison.md`**.

---

## 🚀 Future Enhancements
- Improve **Expert System Rules** for better performance.
- Experiment with **other ML models** (Random Forest, SVM, etc.).
- Deploy a **Streamlit UI** for interactive predictions.

---

## 👨‍💻 Contributors
- **Moataz Ahmed Samir 2305223** – Developer & Researcher & Model Training & Data Preprocessing
- **Team Member 1** – 
- **Team Member 2** – 

---

### Github: https://github.com/Mezo-555/Heart-Disease-Detection-Project.git