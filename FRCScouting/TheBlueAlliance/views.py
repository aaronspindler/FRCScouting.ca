from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/login")
def teaminformation(request):
    return render(request, 'TheBlueAlliance/teaminformation.html')
