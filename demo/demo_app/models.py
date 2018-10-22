from django.db import models
from django.urls import reverse

from kindeditor.models import KindeditorModel
from kindeditor import RichTextField


class ExampleModel(KindeditorModel):
    title = models.CharField(max_length=80, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=80)
    content = RichTextField()

    def get_absolute_url(self):
        return reverse("article-detail", args=(self.pk,))

    def __str__(self):
        return self.title
