# Fraudify Django
##how to install
### cmd  >env\Scripts\ativate
### cmd  >pip install -r requirements.txt
### cmd  > cd Backend
###      >python manage.py migrate
###      >python manage.py runserver
# Register  user</h1>
### url: http://localhost:8000/register/ 
## Request (Post)</h2>
```yaml
{
'username': 'username',
'firstname': 'firstname',
'lastname': 'lastname',
'year':2001,
'month':3,
'day':5,       
'phone':'+919876543210',
'street': 'street',
'locality': 'locality',
'city': 'city',
'country': 'country',
'pincode': 'pincode',
'hint_answer': 'hint_answer',
'login_country': 'login_country',  
'account_number': 'account_number',  
'email': 'email_id',
'password': 'password',
‘image’:Image-file 
}
```
### login_country Should Be in Country Code (like India be IN) 
## Response:
### After Successful Registration
```yaml
{
status": 200,
"message": "Success",
"user_id": "User_Id"
}
```
## Login user
### Request
```yaml
{	
'email':’email,
'password':''password'',
'image':Image_file,
'latitude': 'latitude',                                             
'longitude': 'longitude',
'Up_letter_array': 'Up_letter_array',
'Down_letter_array': 'Down_letter_array',
'Up_time': 'Up_time',
'Down_time': 'Down_time',
'Press_time_array':'Press_time_array',
'otp':Otp_sent_to Mobile,
}
```
### Response:
```yaml
{
    "status": 200,
    "Message": "Login Success",
    "user_id": User_Id,
}
```

## Email Verification
#### http://localhost:8000/verify/email/-Email_Verification_ID-/
### Email_verification_id: 65655b76-45f2-4a8b-ac15-b475c3c49c1c/ 

### Simple Request (Get) To url:
#### http://localhost:8000/verify/email/65655b76-45f2-4a8b-ac15-b475c3c49c1c/

### Response:
```yaml
{
    "status": 200,
    "message": "Email has been verified."
}
```

## Phone Verification
#### http://localhost:8000/verify/phone/
### Request (Post) with User_id and OTP sent to Phone:
```yaml
{
   'id':User_Id,
   'otp':OTP_Sent
}
```

### Response:
```yaml
{
    "status": 200,
    "messages": "Phone Verification Sucess"
}
```

## User Update
#### http://localhost:8000/user/-User.id-/update/
### Request (Post) with User Id in url:
```yaml
{	
'username':'h',
'firstname':'Harish',
'lastname':'Kumar',
'year':2001,'month':3,'day':5,
'phone':'+916383029824',
'street':'velliyanai',
'locality':'main Road',
'city':'kaur',
'country': 'india',
'pincode':'639118',
'hint_answer':'hk',
'login_country':'india',
'account_number':'13111222233334444',
}
```
### Response:
```yaml
{
    "status": 200,
    "messages": "Updation Success"
}
```
## User Delete
#### http://localhost:8000/user/-user.id-/delete/ 
### Request (GET/POST) with User Id in Url: 
#### http://localhost:8000/user/0c010a64-050e-4af3-aeef-7d7d163c81bb/delete/ 

### Response: 
```yaml
{
    "status": 200,
    "messages": "User Account Deleted Sucessfully"
}
```

