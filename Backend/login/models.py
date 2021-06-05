from django.db import models
from .helper import generateUUID
from register.models import User
import random
import hashlib
from datetime import datetime,timedelta

flag_choices = [
    ('0', 'Red'),
    ('1', 'Yellow'),
    ('2', 'Blue'),
    ('3', 'Green'),
]

def time_now():
    return datetime.now()

class KeystrokeDynamics(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    up_letter_array = models.TextField()
    down_letter_array = models.TextField()
    up_time = models.TextField()
    down_time = models.TextField()
    press_time_array = models.TextField()



class LoginVerification(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    otp = models.CharField(max_length=10, editable=True)
    attempts = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT)


class Log(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    datetime = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)
    flag = models.CharField(max_length=1, default='0', choices=flag_choices)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


