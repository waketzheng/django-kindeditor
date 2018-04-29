from django import forms

from kindeditor.fields import RichTextFormField


class KindeditorForm(forms.Form):
    content = RichTextFormField()
