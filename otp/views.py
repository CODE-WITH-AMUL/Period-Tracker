from django.shortcuts import render, redirect
from django.http import JsonResponse
from .otp import generate_otp, verify_otp

def send_otp(request):
    if request.method == 'GET':
        return render(request, 'otp/register.html')
    
    try:
        # Generate OTP
        response = generate_otp(request)
        otp_data = response.json()
        
        # Store OTP details in session
        request.session['otp_secret'] = otp_data.get('otp')
        
        # Pass OTP to template for development/testing
        # In production, you should send this via email/SMS instead
        return render(request, 'otp/verify_otp.html', {
            'otp': otp_data.get('otp'),
            'message': 'OTP sent successfully'
        })
        
    except Exception as e:
        return render(request, 'otp/register.html', {
            'error': str(e)
        })

def verify_otp_view(request):
    if request.method == 'GET':
        return render(request, 'otp/verify_otp.html')
    
    if request.method == 'POST':
        response = verify_otp(request)
        response_data = response.json()
        
        if response_data['status'] == 'success':
            return redirect('registration_success')  # Create this view
        else:
            return render(request, 'otp/verify_otp.html', {
                'error': response_data['message']
            })




