from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import operator
from .models import GameManual

def home(request):
    return render(request, 'ContentPages/home.html')

def about(request):
    return render(request, 'ContentPages/about.html')

def privacy(request):
    return render(request, 'ContentPages/privacypolicy.html')

def terms(request):
    return render(request, 'ContentPages/termsandconditions.html')

def gamemanuals(request):
    gameManuals = GameManual.objects
    return render(request, 'ContentPages/gamemanuals.html',{'gamemanuals':gameManuals})
