# Generated by Django 4.2.4 on 2023-08-25 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0008_alter_images_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='user',
        ),
    ]
