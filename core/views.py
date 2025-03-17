from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse

def index(request):
    return render(request , 'website/index.html')

def Terms(request):
    return render(request , 'accounts/tream.html')

def home(request):
    return render(request , 'website/home.html')

def logininfo(request):
    if request.method == "POST":
        username = request.POST.get('username')
    return render(request , 'website/logininfo.html' , {'username':username})

def save_period(request):
    if request.method == 'POST':
        date = json.laods(request.body)
        PeiodEntry.objects.create(date=date['date'] ,notes=date['notes'])
        return JsonResponse({'status':'success'})
    
    
    