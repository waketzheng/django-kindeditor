from django.conf import settings
from django.http import JsonResponse
from django.utils.translation import gettext as _

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ImageSerializer

SETTINGS_PERMISSION_MAP = {
    "login": (IsAuthenticated,),
    "admin": (IsAdminUser,),
}


def _upload_permission():
    perm = getattr(settings, "KINDEDITOR_UPLOAD_PERMISSION", None)
    return SETTINGS_PERMISSION_MAP.get(perm, ())


class ImageUploadView(APIView):
    permission_classes = _upload_permission()

    def post(self, request):
        serializer = ImageSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            url = request.build_absolute_uri(serializer.data["img"])
            data = {"error": 0, "url": url}
            return JsonResponse(data, status=HTTP_201_CREATED)
        return JsonResponse(
            {
                "error": 1,
                "message": "{}:\n{}".format(
                    _("Upload Error"), serializer.errors
                ),
            },
            status=HTTP_400_BAD_REQUEST,
        )


image_upload = ImageUploadView.as_view()
