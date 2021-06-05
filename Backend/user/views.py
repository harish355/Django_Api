from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime,timedelta
import pytz
from register.models import UserProfile,User,EmailVerification,PhoneVerification,HintQuestions
from login.models import LoginVerification
from register.helper import generateUUID,generateOtp
from register.emails import sendVerificationEmail
from register.phone import sendVerificationMessage
import os

@api_view(["POST", "GET"])
def Update(request,id):
    if(request.method=='POST'):
        try:
            try:
                data=request.data
                username=data['username']
                firstname=data['firstname']
                lastname=data['lastname']
                phone=data['phone']
                street=data['street']
                locality=data['locality']
                city=data['city']
                country=data['country']
                pincode=data['pincode']
                hint_question=HintQuestions.objects.get(id='c38b9f9f-aa55-400d-9df0-587400dd652f')
                hint_answer=data['hint_answer']
                login_country=data['login_country']
                account_number=data['account_number']
                try:
                    image=data['image']
                except:
                    return JsonResponse(data={'status':300,'messages':"image Data Not Provided"})
            except:
                return JsonResponse(data={'status':400,'messages':"Invalid Data Provided"})
            try:
                user=User.objects.get(id=id)
                profile=user.profile
                profile.username=username
                profile.firstname=firstname
                profile.lastname=lastname
                profile.login_country=login_country
                profile.phone=phone
                profile.street=street
                profile.locality=locality
                profile.city=city
                profile.country=country
                profile.pincode=pincode
                profile.hint_answer=hint_answer
                profile.image=image
                if(phone!=profile.phone):
                    otp=generateOtp(6)
                    profile.phone_verified=False
                    PhoneVerification.objects.create(
                    otp=otp,
                    user=user
                    )
                    try:
                        sendVerificationMessage(user.profile.phone, otp) # Check the Twillo Account
                    except:
                        print("OTP Verifcation UnSucessful")
                    profile.save()
                    return JsonResponse(data={'status':200,'messages':"Updation Success "})
                else:
                    profile.save()
                    return JsonResponse(data={'status':200,'messages':"Updation Success "})

            except:
                return JsonResponse(data={'status':400,'messages':"Server Failed"})

        except Exception as e:
            print(e)
            return JsonResponse(data={'status':400,'messages':"Invalid Data Provided"})
    else:
        return JsonResponse(data={"status":400, "message":"Only Get Request Accepted"})

@api_view(["POST", "GET"])
def Delete(request,id):
    if(request.method=="POST" or request.method=='GET'):
            try:
                user=User.objects.get(id=id)
            except:
                return JsonResponse(data={"status":400, "message":"Invalid User id"})
            try:
                EmailVerification.objects.filter(user=user).delete()
            except:
                pass
            try:
                PhoneVerification.objects.filter(user=user).delete()
            except:
                pass
            try:
                LoginVerification.objects.filter(user=user).delete()
            except:
                pass
            try:
                profile=user.profile
                if profile.image:
                    print(profile.image.path)
                    if os.path.isfile(profile.image.path):
                        os.remove(profile.image.path)
                user.delete()
                profile.delete()
            except Exception as e:
                print(e)
                return JsonResponse(data={'status':500,'messages':"Server Error"})
            
            return JsonResponse(data={'status':200,'messages':"User Account Deleted Sucessfully"})
    else:
        return JsonResponse(data={'status':400,'messages':"Only Get/Post Request Accepted"})