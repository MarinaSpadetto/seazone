#!/bin/sh

python manage.py migrate --no-input
python manage.py loaddata ./khanto/fixtures/initial_data.json
python manage.py runserver 0.0.0.0:8000
