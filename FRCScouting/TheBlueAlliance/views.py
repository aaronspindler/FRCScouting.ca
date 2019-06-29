from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import utils

@login_required(login_url="/account/login")
def teaminfo(request):
    if request.method == 'POST':
        teamkey = request.POST['teamnumberinput']
        if(utils.validate_teamkey(teamkey)):
            team = utils.get_teaminfo(teamkey)
            return render(request, 'TheBlueAlliance/teaminformationdetails.html/', {'team': team})
        else:
            error = 'Error: The teamkey was entered in the wrong format!'
            return render(request, 'TheBlueAlliance/teaminformation.html/', {'error': error})
    else:
        return render(request, 'TheBlueAlliance/teaminformation.html')

@login_required(login_url="/account/login")
def teaminfodetails(request, teamkey):
    if(utils.validate_teamkey(teamkey)):
        team = utils.get_teaminfo(teamkey)
        return render(request, 'TheBlueAlliance/teaminformationdetails.html/', {'team': team})
    else:
        error = 'Error: The teamkey was entered in the wrong format!'
        return render(request, 'TheBlueAlliance/teaminformation.html/', {'error': error})
