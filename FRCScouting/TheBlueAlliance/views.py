from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from . import validators, getters

@login_required(login_url="/account/login")
def teaminfo(request):
    if request.method == 'POST':
        teamkey = request.POST['teamnumberinput']
        if(validators.validate_teamkey(teamkey)):
            team = getters.get_team_info(teamkey)
            return render(request, 'TheBlueAlliance/teaminformationdetails.html/', {'team': team})
        else:
            error = 'Error: The teamkey was entered in the wrong format!'
            return render(request, 'TheBlueAlliance/teaminformation.html/', {'error': error})
    else:
        return render(request, 'TheBlueAlliance/teaminformation.html')

@login_required(login_url="/account/login")
def teaminfodetails(request, teamkey):
    if(validators.validate_teamkey(teamkey)):
        team = getters.get_team_info(teamkey)
        return render(request, 'TheBlueAlliance/teaminformationdetails.html/', {'team': team})
    else:
        error = 'Error: The teamkey was entered in the wrong format!'
        return render(request, 'TheBlueAlliance/teaminformation.html/', {'error': error})

@login_required(login_url="/account/login")
def eventinfo(request):
    return render(request, 'TheBlueAlliance/eventinfo.html')

@staff_member_required
def events_loaddata(request):
    getters.get_events_for_year(2016)
    getters.get_events_for_year(2017)
    getters.get_events_for_year(2018)
    getters.get_events_for_year(2019)
    return render(request, 'TheBlueAlliance/admin.html', {'events' : 'Loaded Successfully'})

@staff_member_required
def teams_loaddata(request):
    #TODO : Load Team Data
    return render(request, 'TheBlueAlliance/admin.html', {'teams': 'Loaded Successfully'})
