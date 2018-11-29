from django.contrib import admin

from kindeditor import EditorAdmin
from .models import Article


admin.site.register(Article, EditorAdmin)
