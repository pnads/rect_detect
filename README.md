# Instructions
## Install
1. `poetry install`
1. `poetry shell`

## Run Back End
1. `uvicorn app:app --reload`
1. Go to http://127.0.0.1:8000/docs
1. Expand the POST dropdown then click "Try it out"
1. Choose an image file then click "Execute"

## Run Front End
1. Open 2 terminals
1. Run the back end in one
1. Run the front end: `streamlit run ui.py`
1. Go to http://localhost:8501