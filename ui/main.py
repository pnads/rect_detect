import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")

st.title("RectDetect")

uploaded_file = st.file_uploader("Choose image...", "png", accept_multiple_files=False)

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "image/png")}

if st.button("Extract Vertices"):
    response = requests.post(url=API_URL, files=files)
    with st.expander("Results", expanded=True):
        st.json(response.json(), expanded=True)
