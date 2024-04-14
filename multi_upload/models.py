import os
from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name 


def user_directory_path(instance, filename):
    return "{0}/{1}".format(instance.product.name, filename)

def origin_directory_path(instance, filename):
    return "{0}/origin/{1}".format(instance.promo.vendor, filename)


def sticker_directory_path(instance, filename):
    return "{0}/sticker/{1}".format(instance.vendor, filename)




class Images(models.Model):
    product = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="images"
    )
    image = models.FileField(upload_to=user_directory_path, blank=True)
    img_title = models.CharField(max_length=100, null=True)
    img_price = models.PositiveIntegerField(blank=True, null=True)
    img_description = models.TextField(blank=True, null=True)




class PromoSticker(models.Model):
    vendor = models.CharField(max_length=100)
    promo_image = models.ImageField(upload_to="stickers")




class VendorImage(models.Model):
    vendor = models.CharField(max_length=155, null=True, blank=True)
    vendor_image = models.FileField(upload_to=origin_directory_path,null=True, blank=True)
    promo = models.ForeignKey(PromoSticker, on_delete=models.CASCADE, related_name="vendor_image", null=True, blank=True)




