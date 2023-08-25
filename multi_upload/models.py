import os
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("toys", "toys"),
        ("foods", "foods"),
        ("cosmetics", "cosmetics"),
        ("fashion", "fashion"),
    ]
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES)
    slug = models.CharField(max_length=80, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    return "{0}/{1}".format(instance.product.name, filename)


class ProductsImage(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.product.name
