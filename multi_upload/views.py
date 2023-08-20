import os
from PIL import Image
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from multi_upload.models import Product
from multi_upload.serializers import ProductSerializers


class ProductCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers



class ImageResizeView(APIView):
    def post(self, request):
        res_width = 1500
        input_folder = os.path.join(settings.BASE_DIR, 'media\products')
        output_folder = os.path.join(settings.BASE_DIR, 'media\output')

        for file in os.listdir(input_folder):
            if file.endswith(".jpg") or file.endswith(".png"):
                img = Image.open(os.path.join(input_folder, file))
                wpercent = (res_width / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((res_width, hsize), Image.Resampling.LANCZOS)
                img.save(os.path.join(output_folder, file))

        return Response({'message': 'Images resized successfully'})