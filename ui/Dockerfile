FROM python:3.12-slim

WORKDIR /ui

ENV API_URL="http://api:8000/extract-rect-coords"

COPY ./requirements.txt /ui/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ui/requirements.txt

COPY . /ui

EXPOSE 8501

CMD ["streamlit", "run", "main.py" ]