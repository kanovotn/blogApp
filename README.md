# Blog application
## _The simple blog application written in Django_

This is a project of a simple blog application built using the Django framework
The application provides user logging and registration, blog posts creation and storing posts into the database.
* Register and log in in the web interface
* Add, edit and remove blog posts
* Enjoy reading!

# Getting started
## Prerequisites
Clone the project
```sh
git clone https://github.com/kanovotn/blogApp.git
```
Create Python virtual environment
```sh
python3 -m venv env
source env/bin/activate
```

Run the project locally using the instructions below. By default Django application starts in production mode with
following settings:

| | Debug mode | Database |
| ------ | ------ | ------ |
| **Development** | TRUE | FALSE |
| **Production** | SQLite | PostgreSQL |

## Installation
Install application requirements:
 ```sh
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Usage
Prepare the [database](https://docs.djangoproject.com/en/3.1/ref/settings/#databases) and start the application:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8080 --settings settings.local
```

Test the application, open http://localhost:8080/ in the browser.
# Containers
Containarize application with provided script. You must have Buildah installed as prerequisity.
## Create container
For development use:
```sh
container/build-container-image.sh --devel-use
```
For production use:
```sh
container/build-container-image.sh
```
## Run the image
```sh
podman run -d -p 8080:8080 blogapp
```

# Plugins

Plugins and frameworks used in this project
* [Bootstrap](https://getbootstrap.com/)
* [Ckeditor](https://pypi.org/project/django-ckeditor/)
* [highlight.js](https://highlightjs.org/)
* [Whitenoise](http://whitenoise.evans.io/en/stable/)

# License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.

# Contact
Katerina Odabasi - lyrisha@gmail.com