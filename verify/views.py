from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from register.models import UserProfile,User,EmailVerification,PhoneVerification
from login.models import Sessions
from datetime import datetime,timedelta
import pytz

@api_view(["POST", "GET"])
def email(request,id):
    try:
        email_verification = EmailVerification.objects.get(id=id)
        user = email_verification.user
        user.is_active-True
        user.save()
        email_verification.delete()
        response = {
            'status': 200,
            'message': 'Email has been verified.',
        }
        return JsonResponse(data=response)
    except:
        return JsonResponse(data={'status':400,'messages':"Email Verification Error"})
        
def is_active(id):
    try:
        Session=Sessions.objects.get(Session_Id=id)
        time_now=datetime.now()+timedelta(days=1,seconds=1)  
        time_now=pytz.utc.localize(time_now)  
        print(time_now,Session.time)
        if(Session.time<time_now):
            try:
                Session.time=datetime.now()
                Session.save()
                return True
            except:
                print(JsonResponse(data={"status":502, "message":"Server Error Can't Update expiry time"}))
                return True
        else:
            return False
    except Exception as e:
        print(e)
        return False




@api_view(["POST", "GET"])
def phone(request):
    if(request.method=="POST"):
        try:
            data=request.data
            id=data['id']
            if(is_active(id)==False):
                return JsonResponse(data={'status':300,'messages':"Session Expired Login Again"})
            Session=Sessions.objects.get(Session_Id=id)
            otp_received=data['otp']
            user=Session.user
            phone_verification = PhoneVerification.objects.get(user=user)
            if otp_received == phone_verification.otp:
                phone_verification.delete()
                profile = user.profile
                profile.phone_verified = True
                profile.save()
                return JsonResponse(data={'status':200,'messages':"Phone Verification Sucess"})
            else:
                return JsonResponse(data={'status':300,'messages':"Wrong OTP"})
        except Exception as e:
            print(e)
            return JsonResponse(data={'status':400,'messages':"Email Verification Error"})
    else:
        return JsonResponse(data={'status':500,'messages':"Only Post Request Accepted"})