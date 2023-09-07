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


class Images(models.Model):
    product = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="images"
    )
    image = models.FileField(upload_to=user_directory_path, blank=True)
    img_title = models.CharField(max_length=100, null=True)
    img_price = models.PositiveIntegerField(blank=True,null=True)
    img_description = models.TextField(blank=True, null=True)
