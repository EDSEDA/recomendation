FROM python:3.11-slim

WORKDIR /recommendation

COPY api .
COPY inference .
COPY recommendation .

COPY __init__.py .
COPY config.py .
COPY main.py .

COPY requirements.txt .

RUN pip install -r requirements.txt
