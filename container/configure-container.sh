#!/usr/bin/env bash

# Created on Mon Feb 22 23:12:42 2021
# @author: kanovotn

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080
