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

SETTINGS_PERMISSION_MAP = {"login": {IsAuthenticated}, "admin": {IsAdminUser}}


class APIView(View):
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().dispatch(request, *args, **kwargs)

    def check_permissions(self, request):
        upload = getattr(settings, "KINDEDITOR_UPLOAD_PERMISSION", None)
        upload_perm = SETTINGS_PERMISSION_MAP.get(upload, set())
        permissions = set(self.permission_classes) | upload_perm
        if IsAuthenticated in permissions:
            if not request.user.is_authenticated:
                raise PermissionDenied
        elif IsAdminUser in permissions:
            if not (request.user and request.user.is_staff):
                raise PermissionDenied


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = "__all__"


class ImageUploadView(APIView):
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
