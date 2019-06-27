from django.shortcuts import render

def contactus(request):
    return render(request, 'Contact/contact.html')
