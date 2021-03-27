#!/usr/bin/env bash

# Created on Mon Feb 22 23:12:42 2021
# @author: kanovotn



if [ "$1" == "--local" ]; then
    python3 manage.py makemigrations --settings settings.local
    python3 manage.py migrate --settings settings.local
    python3 manage.py collectstatic --settings settings.local
    python3 manage.py runserver 0.0.0.0:8080 --settings settings.local
else
    python3 manage.py makemigrations
    python3 manage.py migrate
    mkdir -p /opt/blogApp/staticfiles
    python3 manage.py collectstatic
    gunicorn --bind 0.0.0.0:8080 myblog.wsgi
fi
