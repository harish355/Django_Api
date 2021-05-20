# Generated by Django 3.0.5 on 2021-05-17 19:31

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20210518_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image_location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=register.models.image_path),
        ),
    ]