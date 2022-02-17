from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):

    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name

        user.save()

        return redirect('signin')

    return render(request, 'accounts/register.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("logged in")
            return redirect('home')
    
    return render(request, 'accounts/login.html')


def sign_out(request):
    logout(request)
    return redirect('signin')
