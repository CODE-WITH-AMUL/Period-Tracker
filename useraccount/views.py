#------------------------[Importing the libraries]------------------------#
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .otp import send_password_reset_otp  # Updated import

import time
import secrets
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

User = get_user_model()

# ... [keep your existing views for login, register, logout] ...

# Request OTP View
import secrets
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def request_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            
            # Generate 6-digit OTP
            otp = str(secrets.randbelow(999999)).zfill(6)
            
            # Store in session with expiration (5 minutes)
            request.session['reset_otp'] = otp
            request.session['reset_email'] = email
            request.session['otp_created_at'] = str(time.time())  # For expiration
            
            # Print for demonstration (replace with actual email sending)
            print(f"Generated OTP for {email}: {otp}")
            
            messages.success(request, "OTP sent to your email")
            return redirect("verify_otp")
            
        except User.DoesNotExist:
            messages.error(request, "User not found")
    return render(request, "request_otp.html")

# OTP Verification View
def verify_otp(request):
    email = request.session.get("reset_email")
    
    if not email:
        messages.error(request, "Session expired")
        return redirect("request_otp")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")  # Assuming single input field
        try:
            user = User.objects.get(email=email)
            if user.otp == entered_otp:
                # Clear OTP after successful verification
                user.otp = None
                user.save()
                request.session["verified_email"] = email
                return redirect("reset_password")
            messages.error(request, "Invalid OTP")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, "verify_otp.html")

def verify_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        
        # Get session values
        stored_otp = request.session.get('reset_otp')
        email = request.session.get('reset_email')
        otp_time = float(request.session.get('otp_created_at', 0))
        
        # Check expiration (5 minutes)
        if time.time() - otp_time > 300:  # 300 seconds = 5 minutes
            messages.error(request, "OTP has expired")
            return redirect("request_otp")
            
        if not all([stored_otp, email]):
            messages.error(request, "Session expired")
            return redirect("request_otp")
            
        if user_otp == stored_otp:
            # OTP verification successful
            request.session['verified'] = True
            return redirect("reset_password")
            
        messages.error(request, "Invalid OTP")
    return render(request, "verify_otp.html")

# Reset Password View
def reset_password(request):
    email = request.session.get("verified_email")
    
    if not email:
        messages.error(request, "Session expired")
        return redirect("request_otp")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("reset_password")
            
        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            del request.session["verified_email"]
            messages.success(request, "Password reset successfully!")
            return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, "reset_password.html")