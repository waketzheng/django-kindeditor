# django-kindeditor

[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kindeditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/pypi/l/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


This repo is to make it easy to use KindEditor as a RichTextEditor when using django.

You can visit this site to see the editor result: 
http://kindeditor.org/

[Chinese[中文版]](https://github.com/waketzheng/django-kindeditor/blob/master/README.zh-hans.md)

## Requires

- Django 2.0+
- Python 3.6+

## Use

- Install

```
pip install django-kindeditor
```

- Add `kindeditor` and `rest_framework` to INSTALL_APPS in settings

```
INSTALLED_APPS = [
    ...
    'kindeditor',
    'rest_framework',
]
```

## Example

```
# models.py
from kindeditor import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = RichTextField()

# settings.py
KINDEDITOR_UPLOAD_PERMISSION = 'admin'

# admin.py
from django.contrib import admin
from kindeditor import EditorAdmin
from .models import Article
admin.site.register(Article, EditorAdmin)
```

## Demo

1. clone the repo to local

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

4. migrate and compile translation file

```
./manage.py migrate
./manage.py compilemessages
```

5. runserver

```
./manage.py runserver
```

6. view the url and you will see the demo at webbrowser

http://127.0.0.1:8000
