from django.contrib import admin

from kindeditor.admin import EditorAdmin
from .models import ExampleModel


admin.site.register(ExampleModel, EditorAdmin)
