from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ImageSerializer


class ImageUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImageSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            http = 'https://' if request.is_secure() else 'http://'
            host = http + request.get_host()
            data = {'error': 0, 'url': host + serializer.data['img']}
            return JsonResponse(data, status=HTTP_201_CREATED)
        return JsonResponse({
            'error': 1,
            'message': '{}:\n{}'.format(_('Upload Error'), serializer.errors)
        }, status=HTTP_400_BAD_REQUEST)


image_upload = ImageUploadView.as_view()
