from django.urls import path
from .otp import generate_otp, verify_otp
from .views import send_otp, verify_otp_view

urlpatterns = [
    path('generate-otp/', generate_otp, name='generate_otp'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    path('send-otp/', send_otp, name='send_otp'),
]