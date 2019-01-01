# django-kindeditor

[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kindeditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/pypi/l/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)


Django 集成富文本编辑器 KindEditor

KindEditor官网可看到编辑器效果及在线演示：http://kindeditor.org/

## Requires

- Django 2.0+
- Python 3.6+

## Use

- 安装

```
pip install django-kindeditor
```

- 添加 `kindeditor` 到settings中的INSTALL_APPS, 并定义static，media的相关字段

```
INSTALLED_APPS = [
    ...
    'kindeditor',
]
...

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 你的静态文件路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 你的media文件路径
```

- 将"kindeditor/"以及static和media的路径插入到urls.py中的urlpatterns

```
from django.conf import settings

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
