FROM python:2.7

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
