from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.



def home(request:HttpRequest):
    return render(request, 'main_app/home.html')

def terms(request:HttpRequest):
    return render(request, 'main_app/terms.html')