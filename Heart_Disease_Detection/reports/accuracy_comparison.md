# Accuracy Comparison: Expert System vs. Decision Tree Model

## 1️⃣ Validation Set Evaluation
Both the **Rule-Based Expert System** and the **Decision Tree Model** were tested on an unseen validation dataset (`cleaned_data.csv`). Below are the performance results.

## 2️⃣ Performance Metrics
### 📊 **Decision Tree Model Results:**
| Metric      | Score  |
|------------|--------|
| Accuracy   | 0.9854 |
| Precision  | 1.0000 |
| Recall     | 0.9709 |
| F1-Score   | 0.9852 |

### 📜 **Expert System Results:**
| Metric      | Score  |
|------------|--------|
| Accuracy   | 0.5132 |
| Precision  | 0.5132 |
| Recall     | 1.0000 |
| F1-Score   | 0.6783 |

## 3️⃣ Key Findings
✅ **Decision Tree Model** achieved **higher accuracy and precision**, likely due to data-driven learning.  
✅ **Expert System** performed well in recall but had **lower overall accuracy**, suggesting it may generate more false positives.  
✅ **Decision Trees can adapt** to unseen patterns, while the **Expert System relies on predefined rules**, making it less flexible.  

## 4️⃣ Explainability: Decision Tree vs. Expert System
| Feature                    | Decision Tree Model | Expert System |
|---------------------------|-------------------|--------------|
| Data-Driven               | ✅ Yes             | ❌ No        |
| Human Interpretability    | ❌ Limited        | ✅ High      |
| Adapts to New Data        | ✅ Yes             | ❌ No        |
| Consistency in Decisions  | ❌ May vary       | ✅ Always follows rules |

## 5️⃣ Conclusion
The **Decision Tree Model** provides **better accuracy** but lacks explainability, whereas the **Expert System is easier to interpret** but less flexible. Depending on the application, a hybrid approach might be beneficial!

