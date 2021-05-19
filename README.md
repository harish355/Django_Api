# Django_Api
<h1>Register  user</h1>
<h3>url: http://localhost:8000/register/ </h3>
<h2>Request (Post)</h2>
<p>
{'username': 'username',
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
'login_country': 'login_country',  <h3>  #login_country Should Be in Country Code (like India be IN) </h3>
'account_number': 'account_number',  
'email': 'email_id',
'password': 'password',
‘image’:Image-file }
</p>
<h2>Response:</h2>
<h3>After Successful Registration</h3>
<h4>{status": 200,</h4>
<h4>"message": "Success",</h4>
<h4>"Session_Id": "0437305416345148",</h4>
<h4>"user_id": "0c010a64-050e-4af3-aeef-7d7d163c81bb"}</h4>
<h2>Login user<h2>
<h3>Request</h3>
<p>
{	'email':’email,
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
</p>
<h3>Response:</h3>
<p>
{
    "status": 200,
    "Message": "Login Success",
    "Session_Id": "0437305416345148"
}
</p>
<br>
<h2>Email Verification</h2>
<h3>http://localhost:8000/verify/email/<Email_Verification_ID>/</h3>
<h3>Email_verification_id: 65655b76-45f2-4a8b-ac15-b475c3c49c1c/ <h3>
<h4>
Simple Request (Get) To url:</h4><h4>
http://localhost:8000/verify/email/65655b76-45f2-4a8b-ac15-b475c3c49c1c/
</h4>
<h3>Response:</h3>
<p>
{
    "status": 200,
    "message": "Email has been verified."
}
</p>
<br>
<h2>Phone Verification</h2>
<h3>http://localhost:8000/verify/phone/</h3>
<h3>Request (Post) with Session_id and OTP sent to Phone:</h3>
<p>
{'id':Session_Id,
'otp':OTP_Sent
}
</p>
<h3>
Response:</h3>
<p>
{
    "status": 200,
    "messages": "Phone Verification Sucess"
}
</p>

<br>
<h2>User Update</h2>
<h3>
http://localhost:8000/user/<User.id>/update/</h3><h3>
Request (Post) with User Id in url:
</h3>
<p>
{	'username':'h',
'firstname':'Harish',
'lastname':'Kumar',
         'year':2001,'month':3,'day':5,
          'phone':'+916383029824',
'street':'velliyanai',
'locality':'main Road',
'city':'kaur',
'country':      'india',
'pincode':'639118',
'hint_answer':'hk',
'login_country':'india',
         'account_number':'13111222233334444',
         'session_id':'9538215068336738'
}
</p>
<h3>
Response:</h3>
<p>
{
    "status": 200,
    "messages": "Updation Success"
}
</p>
<h2>
User Delete
</h2>
<h3>
http://localhost:8000/user/<User.id>/delete/ </h3><h3>
Request (Post) with User Id in Url: </h3><h3>
http://localhost:8000/user/0c010a64-050e-4af3-aeef-7d7d163c81bb/delete/ </h3>
<p>
{
'session_id':Session_id
}
</p>
<h3>
Response: </h3>
<p>
{
    "status": 200,
    "messages": "User Account Deleted Sucessfully"
}
</p>

