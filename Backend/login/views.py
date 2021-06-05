from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime
from register.models import HintQuestions,UserProfile,User,EmailVerification,PhoneVerification
from login.models import LoginVerification,Log
from .helper import generateUUID,generateOtp,getLocation
from .phone import sendVerificationMessage
from .compare_images import compareImage
import os
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
from .keystroke_dynamics import predict

@api_view(["POST", "GET"])
def Login(request):
    if(request.method=='POST'):
        flag=0
        try:
            data=request.data
            email=data['email']
            print(1)
            password=data['password']
            print(email,password)
            print(2)
            image=data['picture']
            print(image)
            print(3)
            latitude=data['latitude']
            longitude=data['longitude']
            print("Location ",latitude,longitude)
            print(5)
            Up_letter_array=data['Up_letter_array']
            print(Up_letter_array)
            print(6)
            Down_letter_array=data['Down_letter_array']
            print(7)
            Up_time=data['Up_time']
            print(8)
            Down_time=data['Down_time']
            print(9)
            Press_time_array=data['Press_time_array']
            print(10)
            
        except Exception as e:
            print(e)
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
                    log=Log(location=str(latitude)+" "+str(longitude),flag=str(flag),user=user)
                    log.save()
                    return JsonResponse(data={'status':300,'messages':"OTP verification Failed"})
        except:
            print("_______________________OTP is not Provided______________________")
        print()
        # Image
        try:
            if(flag==0):
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
                            flag=1
                            print("____________________________image Verification Success__________________")
                    else:
                        print("Saving Log")
                        log=Log(location=str(latitude)+" "+str(longitude),flag=str(flag),user=user)
                        log.save()
                        
                    os.remove(image_path)
                except Exception as e:
                    print("Image Verification UnSuccess ",e)
                    
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
            
            if(flag==2):
                key_predict=predict(Up_time,Press_time_array)
                if(user.profile.keystroke_prediction==-1):
                    print("New Keystoke Registred")
                    user.profile.keystroke_prediction=key_predict
                    user.profile.save()
                    flag=3
                else:
                    print("Key predection: ",key_predict)
                    if(user.profile.keystroke_prediction==key_predict):
                        flag=3
                        print("Keystoke match Success")
                    else:
                        log=Log(location=str(latitude)+" "+str(longitude),flag=str(flag),user=user)
                        log.save()
                        return JsonResponse(data={'status':300,'flag': flag})


            if flag == 3:
                log=Log(location=str(latitude)+" "+str(longitude),flag=str(flag),user=user)
                log.save()
                try:
                    logs=Log.objects.filter(user=user)
                    for i in logs:
                        if(i.flag=='3'):
                            i.delete()
                except:
                    pass
                return JsonResponse(data={
                    'status': 200,
                    'Message':'Login Success',
                    'user_id':str(user.id)
                })
            else:
                    # Delete existing otp details
                LoginVerification.objects.filter(user=user).delete()
                    # Send otp on phone for red and yellow flag
                phone_verification=PhoneVerification.objects.get(user=user)
                if flag == 1:
                    print("____Flag :1 Sending New OTP")
                    otp_final = generateOtp(8)
                    Login_Verification = LoginVerification.objects.create(
                        otp=otp_final, user=user)
                    phone_verification.otp=otp_final
                else:
                        # Otp for red flag = otp sent (4 digits) + last 4 digits of account number
                    otp = generateOtp(4)
                    print("____Flag :2 Sending New OTP")
                    otp_final = otp + user.profile.account_number[-4:]
                    Login_Verification = LoginVerification.objects.create(
                        otp=otp_final, user=user)
                    phone_verification.otp=otp
                phone_verification.save()

                try:
                    sendVerificationMessage(user.profile.phone, otp_final)    
                except:
                    print("OTP Verifcation UnSucessful")
                log=Log(location=str(latitude)+" "+str(longitude),flag=str(flag),user=user)
                log.save()
                return JsonResponse(data={'status':300,'flag': flag})
        except Exception as e:
            print(e)
            return  JsonResponse(data={'status':300,'message':'Error'})
        
    else:
        user=User.objects.get(email="nhk@gmail.com")
        Login_Verification = LoginVerification.objects.get(user=user)
        print(user,Login_Verification)
        return JsonResponse(data={'status':500,'messages':"Get Requset Not Accpeted"})
    