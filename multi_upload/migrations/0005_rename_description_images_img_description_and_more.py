# Generated by Django 4.2.4 on 2023-09-03 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0004_images_description_images_image_images_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='description',
            new_name='img_description',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='price',
            new_name='img_price',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='title',
            new_name='img_title',
        ),
    ]