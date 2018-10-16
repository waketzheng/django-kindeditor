import os
from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext as _


class KindeditorModel(models.Model):
    content = models.TextField(_("content"))

    class Meta:
        abstract = True


class UploadImage(models.Model):
    img = models.ImageField(
        upload_to=getattr(settings, "KINDEDITOR_UPLOAD_TO", "upload/%Y/%m/")
    )


@receiver(post_delete, sender=UploadImage)
def delete_uploadimg(sender, instance, **kwargs):
    # TO DO: delete img when deleting the related kindeditorModel
    pass


class KindeditorField(models.TextField):
    """
    upload_to: the path to save uploaded images, see Django's ImageFeild
    """

    def __init__(self, verbose_name=None, name=None, upload_to="", **kwargs):
        self.upload_to = upload_to
        super().__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        # TODO: use custom widget
        return super().formfield(**kwargs)
