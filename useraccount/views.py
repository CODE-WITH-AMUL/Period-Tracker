#------------------------[Importing the libraries]------------------------#
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .opt_password import send_otp

User = get_user_model()

#------------------------[Registering the user]------------------------#
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check email existence
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        try:
            # Create user with email as username (assuming custom User model)
            user = User.objects.create_user(
                email=email, 
                password=password
            )
            messages.success(request, "User registered successfully")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return redirect('register')

    return render(request, 'accounts/register.html')

#---------------------[Login system]-----------------#
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using email as username (for custom User model)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
            
    return render(request, 'accounts/login.html')

#-------------------------[logout System]------------------------#
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

#--------------------[OTP Handling]--------------------#

# Request OTP View
def request_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if send_otp(email):  # Assuming email is used as username in send_otp
            request.session["reset_password"] = email
            return redirect("verify_otp")
        messages.error(request, "User not found with this email")
    return render(request, "request_otp.html")

# OTP Verification View
def verify_otp(request):
    email = request.session.get("reset_password")
    
    if not email:
        messages.error(request, "Session expired")
        return redirect("request_otp")

    if request.method == "POST":
        otp_entered = request.POST.get("otp")
        
        try:
            user = User.objects.get(email=email)
            if user.otp == otp_entered:
                return redirect("reset_password")
            messages.error(request, "Invalid OTP")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, "verify_otp.html")

# Reset Password View
def reset_password(request):
    email = request.session.get("reset_password")
    
    if not email:
        messages.error(request, "Session expired")
        return redirect("request_otp")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        
        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)  # Proper password hashing
            user.otp = None  # Clear OTP after successful reset
            user.save()
            del request.session["reset_password"]  # Clean up session
            messages.success(request, "Password changed successfully!")
            return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, "reset_password.html")