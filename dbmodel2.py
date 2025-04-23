import streamlit as st
import joblib
import numpy as np

#Memuat model regresi linear yang sudah disimpan
lin_reg_loaded = joblib.load('lin_reg_model.joblib')

#judul aplikasi
st.title("Prediksi Salary Berdasarkan Years of Experience")

#Input Years of Experience
years_experience = st.number_input("Masukkan Years of Experience:", min_value=0.0, step=0.1)

#Prediksi Salary
if st.button("Prediksi Salary"):
    gaji = lin_reg_loaded.predict([[Years of Experience]])
    st.write(f"Salary seseorang setelah bekerja selama {Years of Experience} tahun adalah ${Salary[0]:,.2f}")