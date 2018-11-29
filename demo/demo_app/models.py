from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from kindeditor import RichTextField


class Article(models.Model):
    title = models.CharField(_("title"), max_length=80)
    content = RichTextField(_("content"))
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("article-detail", args=(self.pk,))

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title
