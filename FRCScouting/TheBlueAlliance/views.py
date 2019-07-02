from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from . import validators, getters

@login_required(login_url="/account/login")
def teaminfo(request):
    if request.method == 'POST':
        teamkey = request.POST['teamnumberinput']
        if(validators.validate_teamkey(teamkey)):
            team = getters.get_team(teamkey)
            return render(request, 'TheBlueAlliance/teaminfodetails.html/', {'team': team})
        else:
            error = 'Error: The teamkey was entered in the wrong format!'
            return render(request, 'TheBlueAlliance/teaminfo.html/', {'error': error})
    else:
        return render(request, 'TheBlueAlliance/teaminfo.html')

@login_required(login_url="/account/login")
def teaminfodetails(request, teamkey):
    if(validators.validate_teamkey(teamkey)):
        team = getters.get_team(teamkey)
        return render(request, 'TheBlueAlliance/teaminfodetails.html/', {'team': team})
    else:
        error = 'Error: The teamkey was entered in the wrong format!'
        return render(request, 'TheBlueAlliance/teaminfo.html/', {'error': error})

@login_required(login_url="/account/login")
def eventinfo(request):
    if request.method == 'POST':
        eventkey = request.POST['eventselector']
        event = getters.get_event(eventkey)
        return render(request, 'TheBlueAlliance/eventinfodetails.html/', {'event': event})
    else:
        all_event_simple = getters.get_all_events_simple()
        events2016 = all_event_simple[2016]
        events2017 = all_event_simple[2017]
        events2018 = all_event_simple[2018]
        events2019 = all_event_simple[2019]
        return render(request, 'TheBlueAlliance/eventinfo.html', {'events2016' : events2016, 'events2017' : events2017, 'events2018' : events2018, 'events2019' : events2019 })

@login_required(login_url="/account/login")
def eventinfodetails(request, eventkey):
    event = getters.get_event(eventkey)
    if event:
        return render(request, 'TheBlueAlliance/eventinfodetails.html/', {'event': event})
    else:
        error = 'Error: The eventkey entered is invalid!'
        return render(request, 'TheBlueAlliance/eventinfo.html/', {'error': error})

@staff_member_required
def events_loaddata(request):
    #TODO : Load Event Data
    return render(request, 'TheBlueAlliance/admin.html', {'events' : 'Loaded Successfully'})

@staff_member_required
def teams_loaddata(request):
    #TODO : Load Team Data
    return render(request, 'TheBlueAlliance/admin.html', {'teams': 'Loaded Successfully'})
