from django.http import JsonResponse
from django.utils.translation import gettext as _
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ImageSerializer


class ImageUploadView(APIView):
    permission_classes = (IsAuthenticated,)

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
