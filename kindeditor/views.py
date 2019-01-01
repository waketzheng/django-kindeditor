from django import forms
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views import View

from .models import UploadImage

HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400
IsAuthenticated = 1
IsAdminUser = 10

SETTINGS_PERMISSION_MAP = {
    "login": (IsAuthenticated,),
    "admin": (IsAdminUser,),
}


def _upload_permission():
    perm = getattr(settings, "KINDEDITOR_UPLOAD_PERMISSION", None)
    return SETTINGS_PERMISSION_MAP.get(perm, ())


class APIView(View):
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        for perm in self.permission_classes:
            if perm == IsAuthenticated:
                if not request.user.is_authenticated:
                    raise PermissionDenied
            elif perm == IsAdminUser:
                if not (request.user and request.user.is_staff):
                    raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = "__all__"


class ImageUploadView(APIView):
    permission_classes = _upload_permission()

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            url = request.build_absolute_uri(obj.img.url)
            data = {"error": 0, "url": url}
            return JsonResponse(data, status=HTTP_201_CREATED)
        return JsonResponse(
            {
                "error": 1,
                "message": "{}:\n{}".format(_("Upload Error"), form.errors),
            },
            status=HTTP_400_BAD_REQUEST,
        )


image_upload = ImageUploadView.as_view()
