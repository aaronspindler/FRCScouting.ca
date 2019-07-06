from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from . import validators
from .team import get_team
from .event import get_event, get_all_events_simple, get_event_teams

@login_required(login_url="/account/login")
def teaminfo(request):
    if request.method == 'POST':
        teamkey = request.POST['teamnumberinput']
        if(validators.validate_teamkey(teamkey)):
            team = get_team(teamkey)
            return render(request, 'TheBlueAlliance/teaminfodetails.html/', {'team': team})
        else:
            error = 'Error: The teamkey was entered in the wrong format!'
            return render(request, 'TheBlueAlliance/teaminfo.html/', {'error': error})
    else:
        return render(request, 'TheBlueAlliance/teaminfo.html')

@login_required(login_url="/account/login")
def teaminfodetails(request, teamkey):
    if(validators.validate_teamkey(teamkey)):
        team = get_team(teamkey)
        return render(request, 'TheBlueAlliance/teaminfodetails.html/', {'team': team})
    else:
        error = 'Error: The teamkey was entered in the wrong format!'
        return render(request, 'TheBlueAlliance/teaminfo.html/', {'error': error})

@login_required(login_url="/account/login")
def eventinfo(request):
    if request.method == 'POST':
        eventkey = request.POST['eventselector']
        event = get_event(eventkey)
        teams = get_event_teams(eventkey)
        teams.sort(key=lambda x: x.team_number)
        if event and teams:
            map_key = settings.GOOGLE_MAPS_KEY
            return render(request, 'TheBlueAlliance/eventinfodetails.html/', {'event': event,'teams': teams, 'map_key':map_key})
        else:
            error = 'Error: The eventkey entered is invalid!'
            return render(request, 'TheBlueAlliance/eventinfo.html/', {'error': error})
    else:
        all_event_simple = get_all_events_simple()
        events2016 = all_event_simple[2016]
        events2017 = all_event_simple[2017]
        events2018 = all_event_simple[2018]
        events2019 = all_event_simple[2019]
        return render(request, 'TheBlueAlliance/eventinfo.html', {'events2016' : events2016, 'events2017' : events2017, 'events2018' : events2018, 'events2019' : events2019 })

@login_required(login_url="/account/login")
def eventinfodetails(request, eventkey):
    event = get_event(eventkey)
    teams = get_event_teams(eventkey)
    teams.sort(key=lambda x: x.team_number)
    if event and teams:
        map_key = settings.GOOGLE_MAPS_KEY
        return render(request, 'TheBlueAlliance/eventinfodetails.html/', {'event': event,'teams': teams, 'map_key':map_key})
    else:
        error = 'Error: The eventkey entered is invalid!'
        return render(request, 'TheBlueAlliance/eventinfo.html/', {'error': error})

@staff_member_required
def admin_controlpanel(request):
    return render(request, 'TheBlueAlliance/admin.html')

@staff_member_required
def events_loaddata(request):
    #TODO : Load Event Data
    return render(request, 'TheBlueAlliance/admin.html', {'message' : 'Events Loaded Successfully'})

@staff_member_required
def teams_loaddata(request):
    #TODO : Load Team Data
    return render(request, 'TheBlueAlliance/admin.html', {'message': 'Teams Loaded Successfully'})
