# RectDetect

See it running live in Google Cloud:

- [Streamlit App](https://rect-detect-ui-zjjnoqowna-nn.a.run.app)
- [Swagger API](https://rect-detect-api-zjjnoqowna-nn.a.run.app/docs)

## Setup and Run Locally

### With Docker

1. Make sure you have Docker Desktop running on your machine and build the container:

   ```bash
   docker compose build
   ```

1. Run the app:

   ```bash
   docker compose up
   ```

1. Go to <http://localhost:8501> for the front end or <http://localhost:8000/docs> for the back end API.

### With Poetry

1. Install [poetry](https://www.python-poetry.org), if not already installed:

   ```bash
   pip install poetry
   ```

1. Navigate to the `rect_detect/` directory and install all dependencies by running:

   ```bash
   poetry install
   ```

1. Activate the virtual environment in your shell:

   ```bash
   poetry shell
   ```

1. Change to the `api/` directory and run the API

   ```bash
   cd api/
   uvicorn main:app --reload
   ``````

1. Go to <http://127.0.0.1:8000/docs> to see the interactive API documentation
   1. You can test the API here by expanding the `POST` dropdown then click "Try it out"
   1. Choose an image file then click "Execute"

1. Open a 2nd terminal in the `rect_detect/` directory and activate the virtual environment (`poetry shell`)

1. Change to the `ui/` directory and run the UI:

   ```bash
   cd ui/
   streamlit run ui.py
   ```

1. Go to <http://localhost:8501> in your browser.
