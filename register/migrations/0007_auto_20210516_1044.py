# Generated by Django 3.0.5 on 2021-05-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_emailverification_phoneverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneverification',
            name='otp',
            field=models.CharField(max_length=10),
        ),
    ]
