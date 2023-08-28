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
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
