# Generated by Django 3.0.11 on 2021-01-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210124_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='location',
            field=models.CharField(default='Delhi, India', max_length=100),
            preserve_default=False,
        ),
    ]
