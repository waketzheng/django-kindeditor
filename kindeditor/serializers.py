from rest_framework.serializers import ModelSerializer

from .models import UploadImage


class ImageSerializer(ModelSerializer):
    class Meta:
        model = UploadImage
        fields = "__all__"
