from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime
from register.models import HintQuestions,UserProfile,User,EmailVerification,PhoneVerification
from login.models import LoginVerification
from .helper import generateUUID,generateOtp,getLocation
from .phone import sendVerificationMessage
from .models import Sessions
from .compare_images import compareImage
import os
from django.core.files.storage import default_storage
from django.conf import settings


@api_view(["POST", "GET"])
def Login(request):
    if(request.method=='POST'):
        try:
            data=request.data
            email=data['email']
            print(1)
            password=data['password']
            print(2)
            try:
                image=data['image']
            except:
                return JsonResponse(data={'status':400,'messages':"Image Data Not provided"})
            print(3)
            try:
                latitude=float(data['latitude'])
                longitude=float(data['longitude'])
            except:
                return JsonResponse(data={'status':400,'messages':"Invaid Latitude/Longitude data provided"})
            print(5)
            Up_letter_array=data['Up_letter_array']
            print(6)
            Down_letter_array=data['Down_letter_array']
            print(7)
            Up_time=data['Up_time']
            print(8)
            Down_time=data['Down_time']
            print(9)
            Press_time_array=data['Press_time_array']
            print(10)
        except:
            return JsonResponse(data={'status':400,'messages':"Invaid Data provided"})
        try:
            user=User.objects.get(email=email)
            if(user.password!=password):
                return JsonResponse(data={'status':300,'messages':"Invalid Password"})
            print("_______________login with Email & Password Sucess_________")
        except:
            return JsonResponse(data={'status':300,'messages':"User Does not Exist"})
        try:
            otp=data['otp']
            if(otp is not None):
                try:
                    print("_____________Checking Opt Db_____________")
                    Login_Verification = LoginVerification.objects.get(user=user)
                    if otp != Login_Verification.otp:
                        return JsonResponse(data={'status':300,'messages':"Wrong OTP"})
                    print("_____________________OTP Verification Success______________-")
                except Exception as e:
                    print("_____________Opt Verification Failed_____________")
                    print(str(e))
                    return JsonResponse(data={'status':300,'messages':"OTP verification Failed"})
        except:
            print("_______________________OTP is not Provided______________________")
        print()
        # Image
        try:
            flag = 0
            try:
                _, image_extension = os.path.splitext(image.name)
                print("Image Extension: ",image_extension,os.path.join(settings.MEDIA_ROOT, 'verify/'))
                image_name = default_storage.save(os.path.join(settings.MEDIA_ROOT, 'verify/'), image)
                print("Image Name: ",image_name)    
                image_path = image_name + image_extension
                print("Image Path: ",image_path)
                os.rename(image_name, image_path)
                print(image_name, image_path)
                if compareImage(image_path, user.profile.image):
                    flag = 1
                os.remove(image_path)
                print("____________________________image Verification Success__________________")
            except Exception as e:
                return JsonResponse(data={'status':400,'messages':"Image Verfication Failed"})
                print("Error at Image Verification ",e)
                pass
            print()
            if flag == 1:
                try:
                    print("___________Checking Location_______________")
                    location = getLocation(latitude, longitude)
                    print("User Location: ",location,user.profile.login_country)
                    if location == user.profile.login_country:
                        flag = 2
                except:
                    print("_______________________Location verification Failed")
            if flag == 2:
                try:
                    Session=Sessions.objects.filter(user=user).latest('time')
                    Session.time=datetime.now()
                    Session.save()
                except Exception as e:
                    print(e)
                    try:
                        _=Sessions.objects.filter(user=user).delete()
                        Session=Sessions(user=user)
                        Session.save()
                    except Exception as e:
                        print(e)
                return JsonResponse(data={
                    'status': 200,
                    'Message':'Login Success',
                    'Session_Id': Session.Session_Id
                })
            else:
                    # Delete existing otp details
                LoginVerification.objects.filter(user=user).delete()
                    # Send otp on phone for red and yellow flag
                if flag == 1:
                    otp = generateOtp(8)
                    Login_Verification = LoginVerification.objects.create(
                        otp=otp, user=user)
                else:
                        # Otp for red flag = otp sent (4 digits) + last 4 digits of account number
                    otp = generateOtp(4)
                    otp_final = otp + user.profile.account_number[-4:]
                    Login_Verification = LoginVerification.objects.create(
                        otp=otp_final, user=user)
                phone_verification=PhoneVerification.objects.get(user=user)
                phone_verification.otp=otp_final
                phone_verification.save()

                #sendVerificationMessage(user.profile.phone, otp) ///////////////////////////////////////////////////////////////////

                return JsonResponse(data={'status':300,'flag': flag})
        except Exception as e:
            print(e)
            return  JsonResponse(data={'status':300,'message':'Error'})
        
    else:
        user=User.objects.get(email="nhk@gmail.com")
        Login_Verification = LoginVerification.objects.get(user=user)
        print(user,Login_Verification)
        return JsonResponse(data={'status':500,'messages':"Get Requset Not Accpeted"})
    