# Generated by Django 4.2.4 on 2023-09-04 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0007_alter_images_img_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='price',
        ),
    ]
