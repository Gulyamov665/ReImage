# Generated by Django 4.2.4 on 2023-09-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0005_rename_description_images_img_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]