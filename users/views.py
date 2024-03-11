from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def user_register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        pic=request.FILES.get('pic')
        try:
            validate_password(password1)
        except ValidationError as error:
            messages.error(request, '\n'.join(error.messages))
            return redirect('users:user_register')
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('users:user_register')
            else:
                user=User.objects.create_user(email=email,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                messages.success(request,'User created successfully')
                return redirect('users:user_login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('users:user_register')        
        
    return render(request, 'register.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('core:index')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('users:user_login')

    return render(request, 'login.html')



def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('core:index')
