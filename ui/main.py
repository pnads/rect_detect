"""
This module contains a Streamlit app for rectangle detection.

It defines a function to detect the vertices of rectangles in an uploaded image using an external API. 
The detected vertices are then displayed in JSON format and as code.

Environment Variables:
- API_URL: The URL of the external API used for detecting vertices.

Example Usage:
1. Run the Streamlit app: `streamlit run main.py`.
2. Upload an image containing rectangles.
3. View the detected vertices in JSON format and as code.

Author: Patrick Nadeau
"""
import os
import asyncio
import aiohttp
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")


async def detect_vertices(uploaded_file: UploadedFile):
    """
    Detects the vertices of rectangles in the uploaded image.

    Args:
        uploaded_file (UploadedFile): The uploaded image file.

    Returns:
        dict: A dictionary containing the coordinates of the detected vertices.

    The function sends the uploaded image to an external API endpoint specified by the `API_URL` environment variable.
    It then processes the response to extract and return the coordinates of the vertices in the form of a dictionary.
    """
    data = {"file": uploaded_file.getvalue()}
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, data=data) as response:
            return await response.json()


st.set_page_config(
    page_title="RectDetect - Find those vertices!",
    layout="wide",
    menu_items={
        "About": "Made by [Patrick Nadeau](https://linkedin.com/in/pnads) for Enurgen\n\n"
    },
)

st.title("RectDetect")

st.markdown("Upload an image of rectangles and get the coordinates of the vertices!")

st.divider()

with st.sidebar:
    uploaded_file = st.file_uploader(
        "Upload an image to process!",
        "png",
        accept_multiple_files=False,
    )

    if uploaded_file:
        with st.container(border=True):
            st.image(
                uploaded_file,
                use_column_width="auto",
            )

with st.container():
    if uploaded_file:
        st.subheader("Detected Vertices")
        tab1, tab2 = st.tabs(["JSON", "Code"])

        vertices = asyncio.run(detect_vertices(uploaded_file))
        if vertices:
            with tab1:
                st.json(vertices, expanded=True)
            with tab2:
                st.code(vertices, language="json")
