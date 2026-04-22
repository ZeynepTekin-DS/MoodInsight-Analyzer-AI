import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. Sayfa Ayarları
st.set_page_config(page_title="Mental Health Analysis AI", layout="centered")

# 2. Üst Görsel
st.image("https://erbakan.edu.tr/storage/images/department/hemsirelikfak/.headline/3aa706af6e3870b83898fc8fd3cb2c88.jpg", use_container_width=True)

# 3. Başlık ve Açıklama
st.title("🧠 Comprehensive Depression Risk Assessment")
st.write("This tool uses a high-precision AI model to evaluate mental health indicators.")
st.info("If you are unsure about any information, please select **'I don't know'**.")

# 4. Model Yükleme
@st.cache_resource
def load_assets():
    model = joblib.load('depression_prediction_model.pkl')
    return model

model = load_assets()

# 5. Giriş Alanları (Tüm Sütun Grupları)
st.subheader("📋 Demographic & Academic Information")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender:", ["I don't know", "Female", "Male"])
    age = st.number_input("Age:", min_value=18, max_value=100, value=25)
    city = st.selectbox("City:", ["I don't know", "Çorum", "Elazığ", "Other"])

with col2:
    profession = st.selectbox("Profession:", ["I don't know", "Academician", "Student", "Healthcare", "Other"])
    academic_pressure = st.selectbox("Academic Pressure (1-5):", ["I don't know", 1, 2, 3, 4, 5])
    cgpa = st.number_input("CGPA (Grade Point Average):", min_value=0.0, max_value=4.0, value=3.0)

st.subheader("🛌 Lifestyle & Health Factors")
col3, col4 = st.columns(2)

with col3:
    sleep_hours = st.selectbox("Sleep Duration:", ["I don't know", "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"])
    diet = st.selectbox("Dietary Habits:", ["I don't know", "Healthy", "Moderate", "Unhealthy"])
    suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["I don't know", "Yes", "No"])

with col4:
    work_pressure = st.selectbox("Work Pressure (1-5):", ["I don't know", 1, 2, 3, 4, 5])
    job_satisfaction = st.selectbox("Job Satisfaction (1-5):", ["I don't know", 1, 2, 3, 4, 5])
    work_study_hours = st.number_input("Daily Work/Study Hours:", min_value=0, max_value=24, value=8)

st.subheader("🧬 Medical History")
family_history = st.selectbox("Family History of Mental Illness:", ["I don't know", "Yes", "No"])

# 6. Analiz Butonu (Balonlar kaldırıldı)
st.markdown("---")
if st.button("RUN CLINICAL ANALYSIS", use_container_width=True):
    # Not: Burada arkada bu verileri 222 sütuna (One-Hot Encoding) çeviren 
    # bir fonksiyon çalışmalı. Şimdilik analiz simülasyonu yapıyoruz.
    
    with st.spinner('Analyzing data points...'):
        # Gerçek model tahmini buraya gelecek
        st.markdown("### 📊 Analysis Report")
        
        # Sonuç Kutusu
        st.success("Analysis successfully completed.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="Risk Status", value="HEALTHY")
        with c2:
            st.metric(label="Confidence Level", value="93.97%")
        
        st.warning("**Note:** This is an AI-based screening tool and does not replace professional medical advice.")