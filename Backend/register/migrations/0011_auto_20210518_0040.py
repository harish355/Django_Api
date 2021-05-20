# Generated by Django 3.0.5 on 2021-05-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_location',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]