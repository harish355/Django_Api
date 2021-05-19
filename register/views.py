from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import datetime
from .models import HintQuestions,UserProfile,User,EmailVerification,PhoneVerification
from login.models import LoginVerification,Sessions
from .helper import generateUUID,generateOtp
from .emails import sendVerificationEmail
from .phone import sendVerificationMessage
import os,os.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'Api.settings'
import re
from django.conf import settings


@api_view(["POST", "GET"])
def index(request):
    if(request.method=='POST'):
        try:
            data=request.data
            d=datetime.date(int(data['year']),int(data['month']),int(data['day']))
            username=data['username']
            print(1)
            firstname=data['firstname']
            print(2)
            lastname=data['lastname']
            print(3)
            birthdate=d
            print(4)
            phone=data['phone']
            print(5)
            street=data['street']
            print(6)
            locality=data['locality']
            print(7)
            city=data['city']
            print(8)
            country=data['country']
            print(9)
            pincode=data['pincode']
            print(10)
            hint_question=HintQuestions.objects.get(id='c38b9f9f-aa55-400d-9df0-587400dd652f')
            print(11)
            hint_answer=data['hint_answer']
            print(12)
            login_country=data['login_country']
            print(13)
            account_number=data['account_number']
            print(14)
            try:
                img=data['image']
            except:
                return JsonResponse(data={'status':300,'messages':"image Data Not Provided"})
            print(15)
            email=data['email']
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
            if(match==None):
                return JsonResponse(data={'status':300,'messages':"Provide a Valid Email Address"})
            print(16)
            password=data['password']
            if(len(password)<7):
                return JsonResponse(data={'status':300,'messages':"Minimum 8 charcter Password"})
        except Exception as e:
            print(e)
            return JsonResponse(data={'status':400,'messages':"Invalid Data Provided"})
        try:
            try:
                profile=UserProfile.objects.get(username=username)
                return JsonResponse(data={'status':300,'messages':"Already an Account Exist with same Username"})
            except:
                pass
            try:
                profile=UserProfile.objects.get(account_number=account_number)
                return JsonResponse(data={'status':300,'messages':"Already an Account Exist with same Account Number"})
            except:
                pass
            try:
                profile=User.objects.get(email=email)
                return JsonResponse(data={'status':300,'messages':"Already an Account Exist with same Email Id"})
            except:
                pass
            newProfile=UserProfile(username=username,firstname=firstname,lastname=lastname,birthdate=birthdate,
            account_number=account_number,hint_answer=hint_answer,
            phone=phone,street=street,locality=locality,city=city,country=country,pincode=pincode,hint_question=hint_question,
            login_country=login_country,image=img)
            newProfile.save()

            print(newProfile)
            user=User(email=email,password=password,profile=newProfile)
            user.save()

            email=EmailVerification(
                user=user,
            )       
            email.save()

            #sendVerificationEmail(email)
            
            otp = generateOtp(6)
            PhoneVerification.objects.create(
                otp=otp,
                user=user
            )
            LoginVerification.objects.create(
                otp=otp,
                user=user,
            )
            Session=Sessions(user=user)
            Session.save()

            #sendVerificationMessage(phone,otp)
            
            return JsonResponse(data={'status':200,'message':'Success',
            'Session_Id':str(Session.Session_Id),'user_id':str(user.id)
            })
        except Exception as e:
             print(e)
             return JsonResponse(data={'status':400,'messages':"Server Error"})

    else:
        return JsonResponse(data={'status':200,'messages':"Get Requset Not Accpeted"})
    