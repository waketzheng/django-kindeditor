from django.urls import reverse
from django.views import generic

from . import forms


class KindeditorFormView(generic.FormView):
    form_class = forms.KindeditorForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse("kindeditor-form")


kindeditor_form_view = KindeditorFormView.as_view()
