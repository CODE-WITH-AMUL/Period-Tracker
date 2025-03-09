# accounts/otp.py
import random
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

def generate_otp():
    """Generate a 6-digit numeric OTP"""
    return str(random.randint(100000, 999999))

def send_password_reset_otp(email: str) -> bool:
    """
    Generate and send OTP for password reset
    Returns True if successful, False otherwise
    """
    try:
        user = User.objects.get(email=email)
        # Generate and save OTP
        user.otp = generate_otp()
        user.save()
        
        # Print simulation (replace with actual email sending)
        print(f"Password reset OTP for {email}: {user.otp}")
        return True
        
    except ObjectDoesNotExist:
        return False
    except Exception as e:
        print(f"Error sending OTP: {str(e)}")
        return False