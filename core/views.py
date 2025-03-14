from django.shortcuts import render

def index(request):
    return render(request , 'website/index.html')

def Terms(request):
    return render(request , 'accounts/tream.html')

def home(request):
    return render(request , 'website/home.html')