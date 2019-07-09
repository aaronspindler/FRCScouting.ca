from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Robot
import datetime

@login_required(login_url="/account/login")
def dashboard(request):
    return render(request, 'Scouting/Dashboard.html')

@login_required(login_url="/account/login")
def robot_add(request):
    if request.method == 'POST':
        robot = Robot()
        robot.team_number = request.POST['team_number']
        robot.year = request.POST['year']
        robot.name = request.POST['name']
        robot.pub_date = datetime.datetime.now()
        robot.submitted_by = request.user
        try:
            robot.image = request.FILES['image']
        except Exception:
            pass

        try:
            robot.image2 = request.FILES['image2']
        except Exception:
            pass

        try:
            robot.image3 = request.FILES['image3']
        except Exception:
            pass

        try:
            robot.image4 = request.FILES['image4']
        except Exception:
            pass

        try:
            robot.image5 = request.FILES['image5']
        except Exception:
            pass

        robot.save()
        return render(request, 'Scouting/Dashboard.html')
    else:
        return render(request, 'Scouting/add_robot.html')
