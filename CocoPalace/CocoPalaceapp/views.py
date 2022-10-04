from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse([{ "msg1" : "Hello" }, { "msg2": "world" }])