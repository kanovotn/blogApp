#!/usr/bin/env bash

# Created on Mon Feb 22 23:12:42 2021
# @author: kanovotn

python3 manage.py makemigrations
python3 manage.py migrate

if [ "$1" == "--local" ]; then
    python3 manage.py runserver 0.0.0.0:8080 --settings settings.local
else
    python3 manage.py runserver 0.0.0.0:8080
fi
