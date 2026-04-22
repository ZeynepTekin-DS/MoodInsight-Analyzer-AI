import streamlit as st
import pandas as pd
import joblib
import numpy as np
from xgboost import XGBClassifier

# --- Page Config ---
st.set_page_config(page_title="Bank Churn AI", page_icon="🏦")

# --- Load Assets ---
@st.cache_resource
def load_model_and_scaler():
    # Ensure these filenames match your saved files exactly!
    model = joblib.load('xgboost_churn_champion_88.pkl')
    scaler = joblib.load('robust_scaler_v1.pkl')
    return model, scaler

model, scaler = load_model_and_scaler()

st.title("🏦 High-Precision Bank Churn Predictor")
st.markdown("---")

# --- User Input UI ---
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 850, 650)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.number_input("Age", 18, 100, 42)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)

with col2:
    balance = st.number_input("Balance (€)", 0.0, 250000.0, 75000.0)
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    has_card = st.selectbox("Has Credit Card? (1=Yes, 0=No)", [1, 0])
    is_active = st.selectbox("Is Active Member? (1=Yes, 0=No)", [1, 0])
    salary = st.number_input("Estimated Salary (€)", 0.0, 200000.0, 120000.0)

# --- Prediction Logic ---
if st.button("🚀 Run AI Analysis"):
    
    # 1. Manual Label Encoding (Must match your Notebook's LabelEncoder)
    geo_map = {'France': 0, 'Germany': 1, 'Spain': 2}
    gender_map = {'Female': 0, 'Male': 1}
    
    # 2. Age Grouping Logic (Matching your pd.cut bins)
    # Bins: [0, 35, 50, 65, 120] -> ['Genç', 'Erişkin', 'Yaşlı', 'Kıdemli']
    # LabelEncoder Order: Erişkin=0, Genç=1, Kıdemli=2, Yaşlı=3
    if age <= 35: age_group_val = 1 
    elif age <= 50: age_group_val = 0 
    elif age <= 65: age_group_val = 3 
    else: age_group_val = 2 

    # 3. Feature Engineering (The 5 extra features)
    balance_per_salary = balance / (salary + 1)
    tenure_by_age = tenure / (age + 1)
    balance_per_product = balance / (num_products + 1)
    active_with_card = is_active * has_card

    # 4. Create DataFrame with EXACT column order as Training
    features_list = [
        'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 
        'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
        'AgeGroup', 'BalancePerSalary', 'TenureByAge', 'BalancePerProduct', 'IsActiveWithCard'
    ]
    
    input_row = [
        credit_score, geo_map[geography], gender_map[gender], age, tenure,
        balance, num_products, has_card, is_active, salary,
        age_group_val, balance_per_salary, tenure_by_age, balance_per_product, active_with_card
    ]
    
    final_df = pd.DataFrame([input_row], columns=features_list)

    # 5. Scaling and Prediction
    try:
        scaled_data = scaler.transform(final_df)
        prediction_proba = model.predict_proba(scaled_data)[0][1]
        
        # --- Visual Output ---
        st.subheader("Result Analysis")
        if prediction_proba > 0.5:
            st.error(f"🚨 HIGH RISK: {prediction_proba*100:.2f}% probability of Churn.")
            st.write("Target this customer with retention campaigns immediately.")
        else:
            st.success(f"✅ LOW RISK: {prediction_proba*100:.2f}% probability of Churn.")
            st.write("Customer is stable. Maintain current engagement.")
            
    except Exception as e:
        st.error(f"Error during prediction: {e}")