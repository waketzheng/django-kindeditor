from django.urls import path

from .views import image_upload

urlpatterns = [path("upload/", image_upload, name="kindeditor-image-upload")]
