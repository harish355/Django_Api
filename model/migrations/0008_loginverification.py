# Generated by Django 3.0.11 on 2021-01-24 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_login_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginVerification',
            fields=[
                ('id', models.CharField(default=users.helper.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('otp', models.CharField(editable=False, max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
