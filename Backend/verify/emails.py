# Functions to send emails for confirmations about registration and updates

from django.core.mail import send_mail
from django.conf import settings
from django.template import loader

from register.models import EmailVerification, User

EMAIL_HOST_USER = settings.EMAIL_HOST_USER
DOMAIN_NAME = settings.DOMAIN_NAME

# Send email for verification at the time of registration
def sendVerificationEmail(email):
    user = User.objects.get(email=email)
    email_verification = EmailVerification.objects.get(user=user)
    from_email = EMAIL_HOST_USER
    # to_list = ['shashankkumar.cse.iitb@gmail.com']
    to_list = [email]
    try:
        html_message = loader.render_to_string(
            template_name='users/verificationEmail.html', 
            context={
                'username': user.profile.username,
                'domain': DOMAIN_NAME,
                'id': email_verification.id
            })
        send_mail(
            'Email verification',
            '',
            from_email,
            to_list,
            fail_silently=False,
            html_message=html_message
        )
    except:
        print(f"Email (type=verification) couldn't be sent to {email}.")

# Send email on every update made to user profile
def sendUpdateEmail(email):
    user = User.objects.get(email=email)
    from_email = EMAIL_HOST_USER
    # to_list = ['shashankkumar.cse.iitb@gmail.com']
    to_list = [email]
    try:
        html_message = loader.render_to_string(
            template_name='users/updateEmail.html', 
            context={
                'username': user.profile.username,
            })
        send_mail(
            'User details updated',
            '',
            from_email,
            to_list,
            fail_silently=False,
            html_message=html_message
        )
    except:
        print(f"Email (type=update) couldn't be sent to {email}.")

# Send email after user account gets deleted successfully
def sendDestroyEmail(email, username):
    from_email = EMAIL_HOST_USER
    # to_list = ['shashankkumar.cse.iitb@gmail.com']
    to_list = [email]
    try:
        html_message = loader.render_to_string(
            template_name='users/deleteEmail.html', 
            context={
                'username': username,
            })
        send_mail(
            'Account deleted',
            '',
            from_email,
            to_list,
            fail_silently=False,
            html_message=html_message
        )
    except:
        print(f"Email (type=destory) couldn't be sent to {email}.")