# Generated by Django 3.0.11 on 2021-02-08 14:32

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_loginverification_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=users.models.image_path),
        ),
    ]