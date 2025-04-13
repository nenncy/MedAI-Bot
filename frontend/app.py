import streamlit as st
import requests

st.title("Discharge Instructions Simplifier")

text_input = st.text_area("Paste Discharge Instruction:")
API_ENDPOINT = "http://localhost:8000/simplify"

if st.button("Simplify"):
    if text_input:
        with st.spinner("Calling backend..."):
            res = requests.post(API_ENDPOINT, json={"text": text_input})
            if res.status_code == 200:
                st.subheader("Simplified Instruction:")
                st.write(res.json()["result"])
            else:
                st.error("Failed to process request")
