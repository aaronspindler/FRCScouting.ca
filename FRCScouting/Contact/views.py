from django.shortcuts import render
from .models import ContactMessage
from datetime import datetime

def contactus(request):
    if request.method == 'POST':
        contactmessage = ContactMessage()
        contactmessage.name = request.POST['name']
        contactmessage.email = request.POST['email']
        contactmessage.subject = request.POST['subject']
        contactmessage.message = request.POST['message']
        contactmessage.sent_date = datetime.now()
        contactmessage.save()
        return render(request, 'Contact/contactsuccess.html')
    else:
        return render(request, 'Contact/contact.html')
