import pyotp
import random
import time
from django.http import HttpResponse
from django.http import JsonResponse

def generate_otp(request):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    otp = totp.now()
    return JsonResponse({
        'status': 'success',
        'otp': otp,
        'message': 'OTP generated successfully'
    })

def verify_otp(request):
    user_otp = request.POST.get('otp')
    secret = request.session.get('otp_secret')
    if not user_otp or not secret:
        return JsonResponse({
            'status': 'error',
            'message': 'OTP or secret not provided'
        })
    totp = pyotp.TOTP(secret)
    if totp.verify(user_otp):
        return JsonResponse({
            'status': 'success',
            'message': 'OTP verified successfully'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid OTP'
        })

if __name__ == '__main__':
    generate_otp()
    