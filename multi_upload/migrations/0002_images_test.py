# Generated by Django 4.2.4 on 2023-08-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='test',
            field=models.CharField(max_length=22, null=True),
        ),
    ]