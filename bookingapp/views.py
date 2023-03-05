from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    if request.user.is_authenticated == False:
        return HttpResponse('Please authorize') 
    return HttpResponse('Home Page')