from rest_framework import serializers
from PIL import Image
from .models import Images, Restaurant
from django.contrib.auth.models import User


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    images = ImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=True, use_url=True),
        write_only=True,
    )

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "user",
            "name",
            "description",
            "price",
            "images",
            "uploaded_images",
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Restaurant.objects.create(**validated_data)

        for image in uploaded_images:
            Images.objects.create(product=product, image=image)

        return product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image", "title", "price", "description"]
