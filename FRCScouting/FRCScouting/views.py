from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import operator

def home(request):
    return render(request, 'home.html')

# def count(request):
#     fulltext = request.GET['fulltext']
#
#     wordlist = fulltext.split()
#     worddictionary = {}
#
#     for word in wordlist:
#         if word in worddictionary:
#             worddictionary[word] += 1
#         else:
#             worddictionary[word] = 1
#
#     sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
#
#     return render(request,'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'privacypolicy.html')

def terms(request):
    return render(request, 'termsandconditions.html')
