import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load Data
df = pd.read_csv("data/cleaned_data.csv")
X = df.drop(columns=["target"])
y = df["target"]

# Split Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter Tuning
param_grid = {
    "max_depth": [3, 5, 10, 11, None],
    "min_samples_split": [2, 5, 10]
}
clf = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
clf.fit(X_train, y_train)
best_model = clf.best_estimator_

# Evaluate Model
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print Results
print("Trained Decision Tree with Best Hyperparameters:", clf.best_params_)
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# Save Model
joblib.dump(best_model, "ml_model/decision_tree_model.pkl")
print("Model saved successfully!")
