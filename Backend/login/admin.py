from django.contrib import admin
from .models import LoginVerification,Log,Sessions

admin.site.register(LoginVerification)
admin.site.register(Log)
admin.site.register(Sessions)
# Register your models here.
