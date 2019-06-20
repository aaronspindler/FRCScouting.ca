from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/signup")
def dashboard(request):
    return render(request, 'Scouting/Dashboard.html')
