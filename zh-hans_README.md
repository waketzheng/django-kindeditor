# django-kindeditor

[![image](https://img.shields.io/pypi/v/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/djversions/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/pypi/pyversions/django-kindeditor.svg)](https://pypi.org/project/django-kineditor/)
[![image](https://img.shields.io/pypi/l/django-kindeditor.svg)](https://pypi.org/project/django-kindeditor/)
[![image](https://img.shields.io/codecov/c/github/waketzheng/django-kindeditor/master.svg)](https://codecov.io/github/waketzheng/django-kindeditor?branch=master)
[![image](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)

> 该仓库已停止更新！鉴于kindeditor的源代码更新频率很低，且用起来的效果跟预期存在一定差距，后续使用富文本一般会用django-ckeditor或vue+quill（参考这个：[panjiachen.github.io/vue-element-admin-site/zh/feature/component/rich-editor.html#常见富文本](https://panjiachen.github.io/vue-element-admin-site/zh/feature/component/rich-editor.html#%E5%B8%B8%E8%A7%81%E5%AF%8C%E6%96%87%E6%9C%AC)）

Django 集成富文本编辑器 KindEditor

KindEditor官网可看到编辑器效果及在线演示：http://kindeditor.org/

## Requires

- Django 2.0+
- Python 3.6+

## Use

- 安装

```bash
pip install django-kindeditor
```

- 添加 `kindeditor` 到settings中的INSTALL_APPS, 并定义static，media的相关字段

```py
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

```py
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

```py
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

# adminx.py (如果采用了xadmin)
import xadmin
from kindeditor import EditorAdminMixin
from .models import Article
admin.site.register(Article, EditorAdminMixin)
```

## Demo

1. 克隆仓库

 ```bash
 git clone https://github.com/waketzheng/django-kindeditor
 ```

2. 创建虚拟环境并安装相应的包

 ```bash
 pipenv install --dev
 ```

3. 激活虚拟环境

 ```bash
 pipenv shell
 ```

4. 生成数据库并编译翻译文件

 ```bash
 ./manage.py migrate
 ./manage.py compilemessages
 ```

5. 启动服务

 ```bash
 ./manage.py runserver
 ```

6. 打开如下网址，即可在浏览器看到效果

 http://127.0.0.1:8000
