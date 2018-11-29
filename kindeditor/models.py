from django.conf import settings
from django.db import models


class UploadImage(models.Model):
    img = models.ImageField(
        upload_to=getattr(settings, "KINDEDITOR_UPLOAD_TO", "upload/%Y/%m/")
    )
