"""Streamlit tests
Run: python3 test_main.py
"""
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("main.py")

at.run()

assert not at.exception
assert at.title[0].value == "RectDetect"
assert at.get("file_uploader")[0]
