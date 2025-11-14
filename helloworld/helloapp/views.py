from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Welcome Hello World!")
# Create your views here.
