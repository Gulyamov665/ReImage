# Generated by Django 5.0.3 on 2024-03-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0016_remove_vendorimage_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorimage',
            name='vendor',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
