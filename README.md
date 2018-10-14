# django-kindeditor

This repo is to make it easy to use KindEditor as a RichTextEditor when using django.

## Do the following steps to see the demo

1. clone the repo the local

```
git clone https://github.com/waketzheng/django-kindeditor
```

2. create a virtual environment and install required packages

```
pipenv install --dev
```

3. activate it

```
pipenv shell
```

4. migrate

```
./manage.py migrate
```

5. create a superuser

```
./manage.py createsuperuser
```

6. runserver

```
./manage.py runserver
```

7. view the url and login with the superuse created abort, then you will see the demo at webbrowser

http://127.0.0.1:8000


## TODOLIST

1. create RichTextField

2. unit test

3. upload to pypi
