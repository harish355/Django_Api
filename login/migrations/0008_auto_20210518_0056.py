# Generated by Django 3.0.5 on 2021-05-17 19:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import login.helper


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20210518_0040'),
        ('login', '0007_auto_20210518_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 18, 0, 56, 47, 513843)),
        ),
        migrations.CreateModel(
            name='KeystrokeDynamics',
            fields=[
                ('id', models.CharField(default=login.helper.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('up_letter_array', models.TextField()),
                ('down_letter_array', models.TextField()),
                ('up_time', models.TextField()),
                ('down_time', models.TextField()),
                ('press_time_array', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.User')),
            ],
        ),
    ]
