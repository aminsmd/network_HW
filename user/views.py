from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user
import json

# Create your views here.

def index(request):
    return HttpResponse("<div> User homepage </div>")

def login(request):
    if(request.method=='POST'):
        #a=json.loads(request.body)
        #print(a)
        print(request.POST)
        for i in user.objects.all() :
            print(i.username)
            if (request.POST["username"] == i.username and request.POST["password"] == i.password) :
                d={"username":i.username , "password":i.password}
                k=json.dump(d)

    return JsonResponse(k)

def logiin(request,un,pw):
    a = user.objects.get(username=un)
    return HttpResponse("<h2>" + un + pw + "</h2>")
