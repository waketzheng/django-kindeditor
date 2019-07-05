# django-kindeditor

[![image](https://secure.travis-ci.org/waketzheng/django-kindeditor.svg?branch=master)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kindeditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/pypi/l/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


This repo is to make it easy to use KindEditor as a RichTextEditor when using django.

You can visit this site to see the editor result:
http://kindeditor.org/

[Chinese[中文版]](https://github.com/waketzheng/django-kindeditor/blob/master/zh-hans-README.md)

## Requires

- Django 2.0+
- Python 3.6+

## Usage

- Install

```
pip install django-kindeditor
```

- Add `kindeditor` to INSTALL_APPS in settings, and define static, media

```
INSTALLED_APPS = [
    ...
    'kindeditor',
]
...

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # your static files path
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # your media files path
```

- Insert "kindeditor/" path and static, media paths to urlpatterns in urls.py

```
from django.conf import settings

if settings.DEBUG:
    # static and media
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns.extend(
        staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
urlpatterns = [
    ...
    path("kindeditor/", include("kindeditor.urls")),
]

if settings.DEBUG:
    # static and media
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns.extend(
        staticfiles_urlpatterns()
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
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

1. Clone the repo to local

    ```
    git clone https://github.com/waketzheng/django-kindeditor
    ```

2. Create a virtual environment and install required packages

    ```
    pipenv install --dev
    ```

3. Activate it

    ```
    pipenv shell
    ```

4. Migrate and compile translation file

    ```
    ./manage.py migrate
    ./manage.py compilemessages
    ```

5. Runserver

    ```
    ./manage.py runserver
    ```

6. View the url and you will see the demo at webbrowser.

    http://127.0.0.1:8000


## Development

1. Test Coverage

  ```
  coverage run ./manage.py test
  ```

2. Test multiple django versions

  ```
  tox
  ```
