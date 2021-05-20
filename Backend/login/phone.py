from django.conf import settings
from twilio.rest import Client

TWILIO_ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
TWILIO_FROM = settings.TWILIO_FROM

# Function to send verification message to given user
def sendVerificationMessage(phone, otp):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Fraudify phone verification OTP - {otp}",
        from_=TWILIO_FROM,
        to=phone
    )