from django.contrib import admin
from .models import HintQuestions,UserProfile,User,EmailVerification,PhoneVerification

admin.site.register(HintQuestions)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(PhoneVerification)
admin.site.register(EmailVerification)
# Register your models here.
