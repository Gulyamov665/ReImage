# Generated by Django 4.2.4 on 2023-08-30 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0002_images_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='description',
        ),
        migrations.RemoveField(
            model_name='images',
            name='image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='price',
        ),
        migrations.RemoveField(
            model_name='images',
            name='test',
        ),
        migrations.RemoveField(
            model_name='images',
            name='title',
        ),
    ]
