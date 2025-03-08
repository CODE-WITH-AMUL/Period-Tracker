#------------------------[Importing the libraries]------------------------#
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
#------------------------[Registering the user]------------------------#
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        try:
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('register')
        user = User.objects.create_user(authenticate , email=email , password=password , confirm_password=confirm_password)
        user.save()
        messages.success(request, "User registered successfully")
        return redirect('login')
    return render(request, 'register.html')

            
#---------------------[Login system]-----------------#
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

#-------------------------[logout System]------------------------#
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('login')