# Generated by Django 3.0.5 on 2021-05-16 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210517_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='time',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 0, 53, 54, 495884)),
        ),
    ]
