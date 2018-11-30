# django-kindeditor

[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/l/django-kinndeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kineditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


This repo is to make it easy to use KindEditor as a RichTextEditor when using django.

You can visit this site to see the editor result: 
http://kindeditor.org/

[Chinese[中文版]](https://github.com/waketzheng/django-kindeditor/blob/master/README.zh-hans.md)

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


## Use it in your django project

1. install

```
pipenv install django-kindeditor
```

2. and add `kindeditor` and `rest_framework` to INSTALLED_APPS in your settings file

```
INSTALLED_APPS = [
    ...
    'kindeditor',
    'rest_framework',
]
```

3. replace `TextField` by `RichTextField` where your want it to be a Kindeditor

```
# models.py
from kindeditor import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = RichTextField()

    def get_absolute_url(self):
        ...

# admin.py
from django.contrib import admin
from kindeditor import EditorAdmin
from .models import Article
admin.site.register(Article, EditorAdmin)
```

4. the forms, views and template can be as follows:

```
# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

# views.py
from .forms import Article, ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(requset.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()
    return render(request, 'create.html', {'form': form})

# create.html
<html>
<body>
    <form method="post">{% csrf_token %}
    {{ form.media }}
    {{ form.as_p }}
    <input type="submit" value="ok">
    </form>
</body>
</html>
```
