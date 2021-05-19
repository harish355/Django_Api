# Generated by Django 3.0.5 on 2021-05-14 19:21

from django.db import migrations, models
import django.db.models.deletion
import register.helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HintQuestions',
            fields=[
                ('id', models.CharField(default=register.helper.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('question', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.CharField(default=register.helper.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(default='', max_length=100)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(blank=True, default='', max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(blank=True, default='', max_length=15)),
                ('phone_verified', models.BooleanField(default=False)),
                ('account_number', models.CharField(max_length=50, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('street', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('hint_answer', models.CharField(max_length=100)),
                ('login_country', models.CharField(max_length=50)),
                ('keystroke_prediction', models.IntegerField(default=-1)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='../media/')),
                ('hint_question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.HintQuestions')),
            ],
        ),
    ]
