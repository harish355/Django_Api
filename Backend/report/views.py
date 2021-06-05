from django.http import JsonResponse
from rest_framework.decorators import api_view
from login.models import Log
import json
from register.models import User


@api_view(["POST", "GET"])
def users(request):
    users=User.objects.all()
    result=json.loads('{}')
    l=[]
    for i in users:
        l.append(i.email)
    temp={'users':l}
    result.update(temp)
    temp={'number':len(l)}
    result.update(temp)
    return JsonResponse(data={'status':200,'messages':result})

@api_view(["POST", "GET"])
def loggedin(request):
    list_user=Log.objects.filter(flag='3')
    result=json.loads('{}')
    greenlist=[]
    for i in list_user:
        greenlist.append([i.user.email,i.datetime])
    temp={'logged_user':greenlist}
    result.update(temp)
    return JsonResponse(data={'status':200,'messages':result})

@api_view(["POST", "GET"])
def login_reports(request):
    list_user=Log.objects.filter(flag='3')
    result=json.loads('{}')
    greenlist=[]
    for i in list_user:
        greenlist.append([i.user.email,i.datetime])
    temp={'green':greenlist}
    result.update(temp)

    #Blue list
    list_user=Log.objects.filter(flag='2')
    bluelist=[]
    for i in list_user:
        bluelist.append([i.user.email,i.datetime])
    temp={'blue':bluelist}
    result.update(temp)

    #Yello list
    list_user=Log.objects.filter(flag='1')
    yellowlist=[]
    for i in list_user:
        yellowlist.append([i.user.email,i.datetime])
    temp={'yellow':yellowlist}
    result.update(temp)
    
    #Red list
    list_user=Log.objects.filter(flag='0')
    redlist=[]
    for i in list_user:
        redlist.append([i.user.email,i.datetime])
    temp={'red':redlist}
    result.update(temp)

    return JsonResponse(data={'status':200,'messages':result})
