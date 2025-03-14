from django.shortcuts import render

def index(request):
    return render(request , 'website/index.html')

def Terms(request):
    return render(request , 'accounts/tream.html')

def home(request):
    return render(request , 'website/home.html')

def logininfo(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass
    return render(request , 'website/logininfo.html' )