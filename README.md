# django-kindeditor

This repo is for the purpose to make it easy to use KindEditor as a RichTextEditor when use django.

You can visit this site to see the editor result: 
http://kindeditor.org/

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

5. runserver

```
./manage.py runserver
```

6. view the url and you will see the demo at webbrowser

http://127.0.0.1:8000


## Use it in your django project

1. copy the `kindeditor` directory to your project

```
git clone https://github.com/waketzheng/django-kindeditor
cp django-kindeditor/kindeditor /path/of/your/project
```

2. install djangorestframework

```
pip install djangorestframework
```

3. and add `kindeditor` and `rest_framework` to INSTALLED_APPS in your settings file

```
INSTALLED_APPS = [
    ...
    'kindeditor',
    'rest_framework',
]
```

4. replace `TextField` by `RichTextField` where your want it to be a Kindeditor

```
# models.py
from kindeditor import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = RichTextField()

    def get_absolute_url(self):
        ...
```

5. the forms, views and template can be as follows:

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
<head>
    {{ form.media }}
</head>
<body>
    <form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="ok">
    </form>
</body>
</html>
```


## TODOLIST

1. unit test

2. upload to pypi
