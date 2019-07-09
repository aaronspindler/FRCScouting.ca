from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RobotUploadForm
from .models import Robot
import datetime

@login_required(login_url="/account/login")
def dashboard(request):
    return render(request, 'Scouting/Dashboard.html')

@login_required(login_url="/account/login")
def robot_add(request):
    if request.method == 'POST':
        filled_form = RobotUploadForm(request.POST)
        if filled_form.is_valid():
            robot = Robot()
            robot.team_number = filled_form.cleaned_data['team_number']
            robot.year = filled_form.cleaned_data['year']
            robot.name = filled_form.cleaned_data['name']
            robot.pub_date = datetime.now()
            robot.submitted_by = request.user
            if filled_form.cleaned_data['image']:
                robot.image = filled_form.cleaned_data['image']
            if filled_form.cleaned_data['image2']:
                robot.image2 = filled_form.cleaned_data['image2']
            if filled_form.cleaned_data['image3']:
                robot.image3 = filled_form.cleaned_data['image3']
            if filled_form.cleaned_data['image4']:
                robot.image4 = filled_form.cleaned_data['image4']
            if filled_form.cleaned_data['image5']:
                robot.image5 = filled_form.cleaned_data['image5']
            robot.save()
        return render(request, 'Scouting/Dashboard.html')


    else:
        form = RobotUploadForm()
        return render(request, 'Scouting/add_robot.html', {'form':form})
