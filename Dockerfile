FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py loaddata ./khanto/fixtures/initial_data.json

EXPOSE 8000
