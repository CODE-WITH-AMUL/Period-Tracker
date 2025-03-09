from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

def send_otp(email: str) -> bool:
    """
    Generate and send OTP to the user's email (simulated).
    
    Args:
        email (str): User's email address
        
    Returns:
        bool: True if OTP sent successfully, False if user not found
    """
    try:
        user = User.objects.get(email=email)
        otp_code = user.generate_otp()  # Assuming this method exists in your User model
        
        # Simulated email sending - replace with real email backend in production
        print(
            f"Auto Email from noreplydjangoft@gmail.com: "
            f"Your OTP for password reset is: {otp_code}"
        )
        return True
        
    except ObjectDoesNotExist:
        return False
    except Exception as e:
        # Consider adding proper error logging here
        print(f"Error sending OTP: {str(e)}")
        return False