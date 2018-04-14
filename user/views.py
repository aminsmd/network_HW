from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user
import time
import json

# Create your views here.

def index(request):
    return HttpResponse("<div> User homepage </div>")

def login(request):
    message = "login unsuccessful"
    if(request.method=='POST'):
        #a=json.loads(request.body)
        #print(a)
        #print(request.POST)
        for i in user.objects.all() :
            if (request.POST["username"] == i.username and request.POST["password"] == i.password) :
                i.loginscu=True
                t = str(int(time.time()))
                i.token = t
                i.save()
                message = "login successful"
                d={"username":i.username , "password":i.password , "balance":i.balance , "login":i.loginscu ,"token":t ,"status":message}
        if (message == "login unsuccessful") :
            i.loginscu=False
            return HttpResponse("<h1> username or password wrong </h1>")
    return JsonResponse(d)

def logiin(request,un,pw):
    a = user.objects.get(username=un)
    return HttpResponse("<h2>" + un + pw + "</h2>")

def balance(request):
    #print(request.GET)
    if (request.method == 'GET'):
        for i in user.objects.all():
            if(request.GET['token']==i.token and i.loginscu==True) :
                #print(i)
                b = {'balance' :str(i.balance)}

    #print(b)
    return JsonResponse(b)

def deposite(request) :
    #print(request.GET)
    if (request.method == 'GET'):
        for i in user.objects.all():
            if(request.GET['token']==i.token and i.loginscu==True) :
                i.balance = int(request.GET["add"]) + i.balance
                new_balance=i.balance
                i.save()
                d = {"new balance": new_balance}
                #print(d)
    return JsonResponse(d)

def withdraw(request):
    if (request.method == 'GET'):
        for i in user.objects.all():
            if(request.GET['token']==i.token and i.loginscu==True) :
                if (i.balance > int(request.GET["wd"])):
                    i.balance = i.balance - int(request.GET["wd"])
                    new_balance = i.balance
                    i.save()
                    d = {"new balance": new_balance , "status": "done"}

                else:
                    new_balance=i.balance
                    d = {"new balance": str(new_balance), "status": "unsuccessful"}
                #print(d)
    return JsonResponse(d)


def logout(request):
    if (request.method == 'GET'):
        for i in user.objects.all():
            if(request.GET['token']==i.token and i.loginscu==True) :
                i.loginscu=False
                i.token=0
                i.save()

                return HttpResponse("logout successful")