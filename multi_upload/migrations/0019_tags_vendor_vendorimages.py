# Generated by Django 5.0.3 on 2024-04-14 11:53

import django.db.models.deletion
import multi_upload.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0018_alter_promosticker_promo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('tag', models.ImageField(blank=True, null=True, upload_to='sticker')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=multi_upload.models.origin_directory_path)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='multi_upload.vendor')),
            ],
        ),
    ]
