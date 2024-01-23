import streamlit as st
import json
import requests

API_URL = "http://127.0.0.1:8000/extract-rect-coords"


st.title("RectDetect")

uploaded_file = st.file_uploader("Choose image...", 'png', accept_multiple_files=False)

if uploaded_file:
    files = {'file': (uploaded_file.name, uploaded_file.getvalue(), "image/png")}

if st.button("Extract Vertices"):
    response = requests.post(url=API_URL, files=files)

    st.json(response.json())