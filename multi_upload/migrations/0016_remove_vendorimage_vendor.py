# Generated by Django 5.0.3 on 2024-03-07 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0015_vendorimage_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorimage',
            name='vendor',
        ),
    ]
