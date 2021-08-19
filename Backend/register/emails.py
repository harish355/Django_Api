# Functions to send emails for confirmations about registration and updates

from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from .models import EmailVerification, User

# Send email for verification at the time of registration
def sendVerificationEmail(email):
    user = User.objects.get(email=email)
    email_verification = EmailVerification.objects.get(user=user)
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    try:
        send_mail(
            'Email verification',
            'Email Varification Link : '+str(settings.DOMAIN_NAME)+'verify/email/'+str(email_verification.id),
            from_email,
            to_list,
            fail_silently=False,
        )
    except Exception as e:
        print("___________________",e)
        print(f"Email (type=verification) couldn't be sent to {email}.")


def sendUpdateEmail(email):
    user = User.objects.get(email=email)
    from_email = EMAIL_HOST_USER
    to_list = [email]
    try:

        send_mail(
            'Email verification',
            'User Updation for '+str(user.Username),
            from_email,
            to_list,
            fail_silently=False,
        )
    except:
        print(f"Email (type=update) couldn't be sent to {email}.")

def sendDestroyEmail(email, username):
    from_email = EMAIL_HOST_USER
    to_list = [email]
    try:
        send_mail(
            'Email verification',
            'Account Deleted Sucessfully ',
            from_email,
            to_list,
            fail_silently=False,
        )
    except:
        print(f"Email (type=destory) couldn't be sent to {email}.")
