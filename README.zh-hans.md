# django-kindeditor

[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/l/django-kinndeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kineditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


Django 集成富文本编辑器 KindEditor

KindEditor官网可看到编辑器效果及在线演示：http://kindeditor.org/

## django-kindeditor的具体使用可看demo

1. 克隆仓库

```
git clone https://github.com/waketzheng/django-kindeditor
```

2. 创建虚拟环境并安装相应的包

```
pipenv install --dev
```

3. 激活虚拟环境

```
pipenv shell
```

4. 生产数据库并编译翻译文件

```
./manage.py migrate
./manage.py compilemessages
```

5. 启动服务

```
./manage.py runserver
```

6. 打开如下网址，即可在浏览器看到效果

http://127.0.0.1:8000


## 安装和使用

1. 安装

```
pipenv install django-kindeditor
```

2. 添加 `kindeditor` 和 `rest_framework` 到settings文件的INSTALLED_APPS 

```
INSTALLED_APPS = [
    ...
    'kindeditor',
    'rest_framework',
]
```

3. 将`TextField` 替换为 `RichTextField`

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

4. forms, views and template 可配置如下:

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
