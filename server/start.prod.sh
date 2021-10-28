#!/bin/bash

python ./manage.py migrate
python ./manage.py collectstatic --clear --noinput
gunicorn --bind 0.0.0.0:8000 prospectsearch.wsgi --workers 3