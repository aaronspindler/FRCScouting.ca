from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django_countries import countries



def signup(request):
    #The user wants to sign up
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'Accounts/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], first_name=request.POST['firstname'], last_name=request.POST['lastname'],country=request.POST['country'], team_number=request.POST['team_number'], email=request.POST['email'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'Accounts/signup.html', {'countries':countries, 'error':'Passwords must match!'})

                #User wants to enter info
    else:
        return render(request, 'Accounts/signup.html', {'countries':countries})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return render(request, 'Accounts/login.html', {'error':'Username/Password is incorrect!'})
    else:
        return render(request, 'Accounts/login.html')

def settings(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.country = request.POST['country']
        if request.POST['team_number']:
            user.team_number = request.POST['team_number']
        user.save()
        return render(request, 'Scouting/Dashboard.html', {'message':'Successfully saved settings'})
    else:
        return render(request, 'Accounts/settings.html', {'countries':countries})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
