from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    print(request.user.is_authenticated)
    return render(request, 'home.html')

def login_handle(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
            return redirect('login-form')
        
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login-form')
