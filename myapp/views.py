from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.   
def home(request):
    return HttpResponse("Home page")
    
def hiname(request, username):
    return HttpResponse("Hi " + username)
    
def age(request, year):
    return HttpResponse("Age: " + str(year))
    
def hello_view(request):
    return render(request, 'plot.html')