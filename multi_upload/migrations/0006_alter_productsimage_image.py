# Generated by Django 4.2.4 on 2023-08-20 07:14

from django.db import migrations, models
import multi_upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0005_productsimage_name_alter_productsimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsimage',
            name='image',
            field=models.ImageField(upload_to=multi_upload.models.Product),
        ),
    ]
