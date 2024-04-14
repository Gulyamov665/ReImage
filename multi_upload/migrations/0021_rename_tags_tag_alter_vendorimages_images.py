# Generated by Django 5.0.3 on 2024-04-14 14:49

import multi_upload.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0020_vendor_tag_alter_vendorimages_vendor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='vendorimages',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=multi_upload.models.original_directory_path),
        ),
    ]
