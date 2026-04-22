🧠 Depression Risk Predictor AI: Biopsychosocial Data Analysis and Early Diagnosis System

APPLICATION LINK (Hugging Face):

 https://huggingface.co/spaces/zeynepptkn/MoodInsight-Analyzer-AI  ---https://github.com/ZeynepTekin-DS/MoodInsight-Analyzer-AI

PROJECT SUMMARY: 📖 This study was developed to predict depression risk with high precision by analyzing individuals' demographic information, academic/professional performance, and lifestyle habits. By processing critical factors such as work pressure, sleep patterns, and family history with machine learning algorithms, the project offers a data-driven early warning mechanism for at-risk groups.
METHODS USED:

Advanced Algorithm (Logistic Regression): 🧠 Among 7 different tested algorithms, Logistic Regression was selected as it modeled the linear relationships between variables most stably and exhibited the highest performance with a 0.9397 F1-Score.

Performance Stability: ⚖️ The model proved its ability to generate reliable predictions on new profiles without overfitting. Thanks to its mathematical stability, it possesses a strong generalization capacity for real-world data.

Class Balancing (SMOTE): 🧬 To address the 81.8% "Non-Depressive" dominance (class imbalance) in the dataset, the SMOTE technique was utilized. The training sample was increased from 112,000 to 184,000, maximizing the model's sensitivity in capturing depression cases.
DATA PREPROCESSING & FEATURE ENGINEERING:

Handling Missing Data: 🧹 Missing data in critical fields such as Academic Pressure, CGPA, and Job Satisfaction were professionally cleaned and processed to maintain model accuracy.

Categorical Encoding: 🛠️ Categorical data such as gender, sleep duration, and dietary habits were converted into numerical formats (Label Encoding/Standardization) that algorithms can process.
KEY RESULTS:

Demographic Sensitivity: 🏆 Analysis revealed that depression is particularly concentrated in the 18-30 age group and, professionally, among teachers.

Critical Triggers: 📊 For working professionals, high work pressure (Level 4 and 5) and irregular sleep hours were proven to be the biggest triggers. Furthermore, the 49.4% suicidal ideation rate in the sample statistically documents the severity of the situation.
NOTES:

Interactive Interface: 🎨 The interface developed with Streamlit accepts information such as age, gender, occupation, and sleep patterns from the user to generate a risk analysis and accuracy rate within seconds.

Production Deployment: ☁️ The model was packaged in .joblib format and deployed live on Hugging Face Spaces, transforming raw data into an end-to-end AI product providing strategic foresight.


Prepared By: Zeynep Tekin

Date: April 13, 2026