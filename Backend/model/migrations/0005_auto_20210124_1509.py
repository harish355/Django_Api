# Generated by Django 3.0.11 on 2021-01-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210124_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='datetime',
        ),
        migrations.AddField(
            model_name='log',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]