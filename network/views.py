from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("<h2> HELLO WORLD </h2>")

def login(request,un,pw):
    return HttpResponse("<h2>" + un + " " + pw + "</h2>")
