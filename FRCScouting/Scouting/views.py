from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Robot
from TheBlueAlliance.team import get_team_events
import datetime

@login_required(login_url="/account/login")
def dashboard(request):
    map_key = settings.GOOGLE_MAPS_KEY
    team_events = None
    if request.user.team_number:
        team_events = get_team_events(request.user.team_number)
        team_events.sort(key=lambda x: x.year, reverse=True)
        team_events = team_events[:9]
    return render(request, 'Scouting/Dashboard.html', {'team_events':team_events, 'map_key':map_key})

@login_required(login_url="/account/login")
def match_scouting(request):
    return render(request, 'Scouting/match_scouting.html')

@login_required(login_url="/account/login")
def pit_scouting(request):
    return render(request, 'Scouting/pit_scouting.html')

@login_required(login_url="/account/login")
def robot_add(request):
    if request.method == 'POST':
        if request.POST['team_number'] and request.POST['year'] and request.POST['name']:
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
            message = 'Your images have been successfully submitted, once they are approved they will show up!'
            return render(request, 'ContentPages/robots.html', {'message':message})
    return render(request, 'Scouting/add_robot.html')

@login_required(login_url="/account/login")
def robots(request):
        approved_robots = []
        all_robots = Robot.objects.all()
        for robot in all_robots:
            if robot.is_approved:
                approved_robots.append(robot)
        return render(request, 'Scouting/robots.html', {'robots':approved_robots})
