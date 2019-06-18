from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import operator
from .models import GameManual

def home(request):
    return render(request, 'ContentPages/home.html')

def permission_denied(request, exception):
    return render(request, 'ContentPages/403.html')

def page_not_found(request, exception):
    return render(request, 'ContentPages/404.html')

def server_error(request):
    return render(request, 'ContentPages/500.html')

def about(request):
    return render(request, 'ContentPages/about.html')

def privacy(request):
    return render(request, 'ContentPages/privacypolicy.html')

def licenses(request):
    return render(request, 'ContentPages/licenses.html')

def contact(request):
    return render(request, 'ContentPages/contact.html')

def gamemanuals(request):
    gameManuals = GameManual.objects
    return render(request, 'ContentPages/gamemanuals.html',{'gamemanuals':gameManuals})

def pitscouting(request):
    return render(request, 'ContentPages/pitscouting.html')

def matchscouting(request):
    return render(request, 'ContentPages/matchscouting.html')

def whyads(request):
    return render(request, 'ContentPages/why-ads.html')
