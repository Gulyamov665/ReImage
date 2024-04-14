from rest_framework import serializers
from PIL import Image
from .models import Images, Restaurant, PromoSticker, VendorImage
from django.contrib.auth.models import User
from rest_framework.response import Response


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class VendorImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorImage
        fields = "__all__"


class PromoSerializers(serializers.ModelSerializer):
    vendor_image = VendorImagesSerializer(many=True, read_only=True, allow_null=True)
    origin_images = serializers.ListField(
        child=serializers.FileField(allow_empty_file=True, use_url=True),
        write_only=True,
        required=False
    )

    class Meta:
        model = PromoSticker
        fields = ["vendor_image", "origin_images","vendor", ]

    def create(self, validated_data):
        origin_images = validated_data.pop("origin_images")
        promo_id = PromoSticker.objects.get(id=73)

        for image_data in origin_images:
            VendorImage.objects.create(
                vendor_image=image_data,
                promo=promo_id
            )

        return promo_id
    


class Promo(serializers.ModelSerializer):
    class Meta:
        model = PromoSticker
        fields = ["id", "vendor", "promo_image"]

class ProductSerializers(serializers.ModelSerializer):
    images = ImageSerializers(many=True, read_only=True, allow_null=True)
    uploaded_images = serializers.ListField(
        child=serializers.FileField(allow_empty_file=True, use_url=True),
        write_only=True,
    )
    title = serializers.ListField(child=serializers.CharField(), write_only=True)
    img_price = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
    )
    img_desc = serializers.ListField(
        child=serializers.CharField(
            allow_blank=True,
            allow_null=True,
            required=False,
        ),
        write_only=True,
        allow_empty=True,
        required=False,
    )

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "user",
            "name",
            "description",
            "images",
            "uploaded_images",
            "title",
            "img_price",
            "img_desc",
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        titles = validated_data.pop("title")
        prices = validated_data.pop("img_price")
        img_descriptions = validated_data.pop("img_desc", [])
        product = Restaurant.objects.create(**validated_data)

        for i, image in enumerate(uploaded_images):
            title = titles[i] if i < len(titles) or i <= 0 else "None"
            price = prices[i] if i < len(prices) or i <= 0 else 0
            desc = img_descriptions[i] if i < len(img_descriptions) or i <= 0 else ""
            Images.objects.create(
                product=product,
                image=image,
                img_title=title,
                img_price=price,
                img_description=desc,
            )

        return product


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ["image", "img_title", "img_price", "img_description"]

        img_title = serializers.CharField()
