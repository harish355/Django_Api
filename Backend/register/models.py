from django.db import models
from .helper import generateUUID
import os
import hashlib
os.environ['DJANGO_SETTINGS_MODULE'] = 'Api.settings'

from django.conf import settings

class HintQuestions(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    question = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.question

def image_path(self, filename):
    # Check if the directory structure exists
    media_dir = settings.MEDIA_ROOT
    if (not os.path.isdir(media_dir)):
        os.mkdir(media_dir)
    # Check if the file format is one of the following
    _, extension = os.path.splitext(filename)
    if (extension in ['.png', '.jpg', '.jpeg']):
        # Get the hash of the file
        file = self.image.open()
        data = file.read()
        filehash = hashlib.md5(data)
        return f'{media_dir}/{filehash.hexdigest()}{extension}'
    else:
        return f'{media_dir}/default.png'

class UserProfile(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    username = models.CharField(max_length=100, default='')
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    birthdate = models.DateField(blank=True)
    # Phone details
    phone = models.CharField(max_length=15, blank=True, default='')
    phone_verified = models.BooleanField(default=False)
    # Account details
    account_number = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    # Address = Street, Locality, City, Country, Pincode
    street = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    # Answer to the hint question
    hint_question = models.ForeignKey(HintQuestions, on_delete=models.PROTECT)
    hint_answer = models.CharField(max_length=100)
    # Location for last login attempt
    login_country = models.CharField(max_length=50)
    # Keystroke dynamics of the user
    # keystroke_dynamics = models.ForeignKey(
    # on_delete=models.deletion.PROTECT, to='users.KeystrokeDynamics')
    keystroke_prediction = models.IntegerField(default=-1)
    # Image of the user
    image = models.ImageField(upload_to=image_path,
                              null=True, blank=True, max_length=500)
    class Meta:
        db_table="UserProfile"
    def __str__(self):
        return "User "+self.id

class User(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    email = models.EmailField(max_length=100, default='', unique=True)
    password=models.CharField(max_length=128,blank=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.PROTECT,blank=True)
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.email+" "+str(self.id)

    class Meta:
        db_table="User"

class EmailVerification(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email+" "+str(self.id)

class PhoneVerification(models.Model):
    id = models.CharField(default=generateUUID, primary_key=True,
                          max_length=36, unique=True, editable=False)
    otp = models.CharField(max_length=10, editable=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.otp
