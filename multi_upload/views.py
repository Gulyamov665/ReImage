import os
from PIL import Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from multi_upload.models import Images, Restaurant
from multi_upload.serializers import ProductSerializers
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers


class ImageResizeView(APIView):
    def post(self, request):
        result = request.data.get("res")
        res_width = 1500
        input_folder = os.path.join(settings.MEDIA_ROOT, str(result))
        output_folder = os.path.join(settings.MEDIA_ROOT, "output", str(result))
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        name = 0

        for file in os.listdir(input_folder):
            name += 1
            filename = str(name)
            files = (".jpg", ".png", ".jpeg", ".webp", ".jfif")
            if file.endswith(files):
                img = Image.open(os.path.join(input_folder, file))
                wpercent = res_width / float(img.size[0])
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((res_width, hsize), Image.Resampling.LANCZOS)
                try:
                    img.save(os.path.join(output_folder, filename + ".jpg"))
                except OSError:
                    img.save(os.path.join(output_folder, filename + ".png"))

        return Response({"message": "Images resized successfully"})


class ImagesApiView(ModelViewSet):
    queryset = Images.objects.all()
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers


class DetailUserApiView(ListAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers

    def get_queryset(self):
        user = self.kwargs["user_id"]
        queryset = Restaurant.objects.filter(user_id=user)
        return queryset


class DetailAllApiView(ListAPIView):
    parser_class = [MultiPartParser, FormParser]
    queryset = Restaurant.objects.all()
    serializer_class = ProductSerializers


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Create": "api/create",
        "Detail/user": "api/detail/<int:user_id>",
        "Detail/all": "api/detail",
        "Create User": "api/create_user",
        "Resize": "api/resize_image",
    }
    return Response(api_urls)
