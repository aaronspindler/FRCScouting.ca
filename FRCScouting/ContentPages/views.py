from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import operator

def about(request):
    return render(request, 'ContentPages/about.html')

def privacy(request):
    return render(request, 'ContentPages/privacypolicy.html')

def terms(request):
    return render(request, 'ContentPages/termsandconditions.html')

def gamemanuals(request):
    return render(request, 'ContentPages/gamemanuals.html')
