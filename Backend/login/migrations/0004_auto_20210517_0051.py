# Generated by Django 3.0.5 on 2021-05-16 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210517_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='time',
            field=models.DateField(default=datetime.date(2021, 5, 17)),
        ),
    ]