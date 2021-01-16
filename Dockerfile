FROM python:3.8.5

COPY . app/

WORKDIR /app

RUN pip install -r requirements/dev.txt