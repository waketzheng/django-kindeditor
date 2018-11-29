from django.conf import settings
from django.db import models

DEFAULT_UPLOAD_TO = "upload/%Y/%m/"


class UploadImage(models.Model):
    img = models.ImageField(
        upload_to=getattr(settings, "KINDEDITOR_UPLOAD_TO", DEFAULT_UPLOAD_TO)
    )
