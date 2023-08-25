import os
from PIL import Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from multi_upload.models import Images, Restaurant
from multi_upload.serializers import ProductSerializers, UserSerializer
from django.contrib.auth.models import User


class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers


class ImageResizeView(APIView):
    def post(self, request):
        user = request.user
        res_width = 1500
        input_folder = os.path.join(settings.MEDIA_ROOT, str(user.username))
        output_folder = os.path.join(settings.MEDIA_ROOT,'output', str(user.username))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for file in os.listdir(input_folder):
            if file.endswith(".jpg") or file.endswith(".png"):
                img = Image.open(os.path.join(input_folder, file))
                wpercent = (res_width / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((res_width, hsize), Image.Resampling.LANCZOS)
                img.save(os.path.join(output_folder, file))

        return Response({'message': 'Images resized successfully'})
    

class DetailUserApiView(ListAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

    def get_queryset(self):
        user = self.kwargs['user_id']
        queryset = Restaurant.objects.filter(user_id=user)
        return queryset
    

class DetailAllApiView(ListAPIView):
    parser_class = [MultiPartParser, FormParser]
    queryset = Restaurant.objects.all()
    serializer_class = ProductSerializers



class UserCreateAPI(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = UserSerializer


class DetailUserApiView(ListAPIView):
    parser_class = [MultiPartParser, FormParser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
    'Create' : 'api/create',
    'Detail/user' : 'api/detail/<int:user_id>',
    'Detail/all' : 'api/detail',
    'Create User' : 'api/create_user',
    'Resize' : 'api/resize_image',
    }
    return Response(api_urls)