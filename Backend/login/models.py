from django.db import models
from .helper import generateUUID
from register.models import User
import random
import hashlib
from datetime import datetime,timedelta
flag_choices = [
    ('0', 'Red'),
    ('1', 'Yellow'),
    ('2', 'Green'),
]

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

def RandomSesssionKey():
     return ''.join([f'{random.randint(0,9)}' for _ in range(16)])

def time():
    time_now=datetime.now()
    session_time=time_now+timedelta(seconds=86400)
    return session_time
def time_now():
    return datetime.now()

class Sessions(models.Model):
      Session_Id=models.CharField(max_length=33,primary_key=True,unique=True,default=RandomSesssionKey)
      time=models.DateTimeField(default=time_now)#auto_now_add=True)
      user=models.ForeignKey(User, on_delete=models.PROTECT)

      def __str__(self):
         return str(self.Session_Id)+str(self.time)

      class Meta:
         db_table="Session"

