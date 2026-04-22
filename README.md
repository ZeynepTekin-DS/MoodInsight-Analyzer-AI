🏦 ChurnGuard-AI: Data Mining-Based Bank Customer Churn Prediction System

APPLICATION LINK (Hugging Face):

 https://huggingface.co/spaces/zeynepptkn/Deep-Churn-Predictor  ---https://github.com/ZeynepTekin-DS/-Deep-Churn-Predictor

PROJECT SUMMARY: 📖 This study was created to predict customer churn, one of the most critical business problems in the banking sector, and to develop loyalty strategies. By analyzing demographic data, financial behaviors, and account movements, the project offers an end-to-end machine learning solution that identifies which customers are inclined to leave the bank with high precision.
METHODS USED:

Champion Model (XGBoost): 🧠 At the core of the project, XGBClassifier, the most advanced version of the gradient boosting decision trees algorithm, was utilized. Configured with optimized hyperparameters such as learning_rate=0.03, n_estimators=1000, and max_depth=6, the model was customized to decode complex customer behaviors.

Performance Excellence: ⚖️ The model exhibited elite performance, achieving an AUC (Area Under the Curve) score of 0.88970 (88.97%) on the validation set. Thanks to the early_stopping_rounds=100 mechanism, the training process was automatically optimized, preventing overfitting and mathematically proving high generalization capacity.
DATA PREPROCESSING & FEATURE ENGINEERING:

Strategic Feature Engineering: 🖇️ To increase the predictive power of the dataset, 5 new synthetic features were derived, including BalancePerSalary, TenureByAge, BalancePerProduct, and IsActiveWithCard. This allowed the model to capture "loyalty signals" hidden within the raw data.

Outlier Stabilization: 🛠️ RobustScaler technology was used to prevent outliers from disrupting the model's balance. Numerical variables were normalized using this method, ensuring the model operates with stable, noise-free input.
KEY RESULTS:

High Precision Inference: 🏆 With an F1-score of 0.8565, the model identifies not just the general audience but also the "high-risk" segments—the primary cost for the bank—with a balance of over 85%.

Critical Insights: 📊 Analysis revealed that the highest risk profile consists of female customers located in Germany, and churn rates reach the 80-90% band in segments with 3 or more products. Additionally, a 60% loss rate in the "Senior" age group was identified as a non-linear effect of age and was successfully decoded by the model.
NOTES:

Interactive Interface: 🎨 Thanks to the user-friendly interface developed with Streamlit, when customer information (age, balance, country, etc.) is entered, the AI calculates the churn probability in seconds and reflects the risk status on the screen with visual feedback.

Production Deployment: ☁️ The model architecture and scaling parameters were optimized in .pkl format and deployed live on Hugging Face Spaces. This work represents the transformation of an academic data analysis process into a functional "Financial Decision Support System."

    [!IMPORTANT]

    Model Storage Notice: Due to GitHub's file size limits, the trained model file is hosted on Hugging Face. You can access the fully functional application and the model via the link provided at the top of this page.

Prepared By: Zeynep Tekin

Date: April 15, 2026