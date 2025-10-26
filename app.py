# app.py
import streamlit as st
import requests

st.title("📊 Stock Portfolio Rebalancer App")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    st.write("File uploaded. Click analyze.")

    if st.button("Analyze"):
        files = {"file": uploaded_file}
        res = requests.post("http://127.0.0.1:8000/analyze", files=files)

        if res.status_code == 200:
            st.subheader("✅ Recommendations:")
            st.write(res.json()["recommendation"])
        else:
            st.error("Error calling backend")