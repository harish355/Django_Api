from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from register.models import EmailVerification, User

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

# Send email on every update made to user profile
def sendUpdateEmail(email):
    user = User.objects.get(email=email)
    from_email = EMAIL_HOST_USER
    # to_list = ['shashankkumar.cse.iitb@gmail.com']
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

# Send email after user account gets deleted successfully
def sendDestroyEmail(email, username):
    from_email = EMAIL_HOST_USER
    # to_list = ['shashankkumar.cse.iitb@gmail.com']
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