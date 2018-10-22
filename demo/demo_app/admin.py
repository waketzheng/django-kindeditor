from django.contrib import admin

from kindeditor import EditorAdmin
from .models import ExampleModel, Article


admin.site.register(ExampleModel, EditorAdmin)
admin.site.register(Article, EditorAdmin)
