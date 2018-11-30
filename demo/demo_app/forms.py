from django import forms

from kindeditor.fields import RichTextFormField

from .models import Article


class KindeditorForm(forms.Form):
    content = RichTextFormField()


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
